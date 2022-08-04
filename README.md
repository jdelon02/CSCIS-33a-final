# CSCIS-33a-final

This project was essentially to take the [Recipe project](https://github.com/jdelon02/cs50Final) I did in Flask for CS50 and Django-fy it.  I also wanted to really try and get a better understanding of the MVC model while leveraging Django's built in Class based approach.  There were several features that the Flask version had:
1. Register/Login/Logout functionality - For Django project, this was baked in.
2. The ability to view a masonry style grid of Recipes.  
3. The ability to "flag" recipes and "save" them for later viewing.
4. A detail page of a recipe, giving more info then the Masonry style display.
5. The ability to search for recipes by title.

## My Approach:

I am a big fan of separation by purpose, and have found the one page for all views, one for all models, etc... very hard to keep track of.  So, I found out (actually in earlier projects) to split the views into their own folder, each being their own file.  Same with the models, and forms.  While there is some overlap of include directives, I have come to prefer this approach since it lets me view each thing on it's own.

## Things that I thought would work, but didn't.  

It may seem strange to start with this, but the reality is that I (again), overthought the structure.  I originally had foreign key fields all over the place, and that caused a lot of problems with my form pages.  Part of that was because I wanted to limit choices the user could make; i.e. I only want them to choose certain options that make sense, but in reality don't change all that much.  So, for example, I originally had a Quantity field as FK on Ingredients model, but the default behavior does not work because there are no initial values in the db.  So, I switched that to a ChoiceField and set the options in the model.  Originally, I had actually built "fixtures" that would need to be run after migration to establish default vals in DB, but didn't like that approach, since it was a lot more cumbersome feeling.  There were a lot of those...

The other area that I really had a hard time with was wanting to allow dynamic ingredients on create/edit recipe forms.  I spent a LOT of time trying to get that to work the way I wanted.  In the end, it is still a little buggy.  The default of doing it via the js lib I found (which is included in static since I ended up editing it a bit), was that it adds an empty row for both ingredients and steps, but if you leave them empty, it throws an error.  So, you have to remember to remove them prior to hitting save.  Annoying.  But, I ran out of time to try and get it to work w/o issue.

### The Models:
**User** - Did not need to do much to this, just add a field for recipes the user has "bookmarked", an fk to recipes.  Added a last login, and date joined field, but decided against doing anything with them at this point.
**Ingredients** - A collection of pre-defined choices and fields that allow for adding a specific "ingredient" and all the related fields for that, to a recipe.
**Steps** - Really just a textarea field with an fk to a recipe.  Step 1, chop all ingredients, Step 2, turn on Oven to 350.  etc...
**Recipes** - This model was the real workhorse of the show.  It has fields for the "per-recipe" specifics.  These are textfields, choicefields, fks, m2m, and a filefield.  
**Userfollowing** - Deprecated.

### The Forms:
**User Form** - Nothing special, just returns the user.
**Ingredient Form** - Creates the default values for all of the forms fields.  Was actually happy that I could leverage this in views as "formset=x", rather than having to list out each field I wanted to include.  
**Steps Form** - Nothing special, just returns a step.
**Recipes Form** - This was the form that gets the most use.  It does a lot of what the ingredients form does, in that it creates default values, establishes field/widget types, and also has two inline_formsetfactories that allow for adding the ingredients and steps on the same frontend form.
I had considered making the "edit" page a single page operation using js, but with the nested formsets, I decided that just wouldn't make sense.

### The Views:

***User View***
This was the only form that I did not fully switch over to a "class-based" approach.  Part of that was a time determination, and part of it was that this was provided for us, and I did not know if it would cause problems.

***Ingredients View***
Originally, during dev, I was using this form as a way to test if things were getting created correctly.  I can't think of any use case for needing this form now, so I have removed the URL pattern to access.

***Templates***
All of the templates use bootstrap5.  I also leveraged several django packages, to either write less styling, or to leverage bootstrap abilities.  I used masonry grid with boostrap cards to create a pinterest style feel throughout.

***Static***
I manage to build the site using only 2 or 3 css changes.  Part of that was due to just actually liking most of the default bootstrap styling.  But, it was also possible because of the packages I leveraged that allowed me to not need to overwrite as much as I was expecting.

There is a "media" directory, which has 2 default images in it.  I am .gitignoring the images folder within, which is where user uploaded images would live.

***Recipe View***
This is the view that does most of the work.  There is a default index(listview) class, which renders the homepage, a bookmark(listview), the creation class, the update class, etc...  I was able to leverage the slight differences in classes to limit the number of templates I needed.  So, for example, the index page and the bookmark page both use the same template, but the queryset returns different results to each.  

I also wanted to incorporate some of the functionality from the "Network" homework, wherein users could "like" recipes, and also wanted the abiltiy to "bookmark" recipes for later.  The AJAX written for Network assigment relied on exempting the csrf.  In order to make this work using classes, I had to move those functions into classes, and then had to rework the ajax to pass the cert.  So, those now operate correctly using a django/js lib that actually was pretty easy to implement.   

## Things I did not get to do
I did not get the ingredient and step formset working as seamlessly as I would have liked.

If I had to do this again, I would try and do a full DB diagram first.  I think the functionality behind this simple program could be expanded to include scraping Recipes Sites, creating Grocery Lists, etc... but I would want to redo some of the structure to better accomodate that.



