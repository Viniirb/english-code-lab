# My review

## S1
nit: could we use a clearer name than d? Maybe calculatePrice would explain the idea. What do you think about 1.2? A named constant would help.

## S2
I think this can crash when the user is not found, because find returns undefined. Could we check the value before we read the name?

## S3
These two lines look very similar. Maybe we can move the logic into one small function and pass the list as an argument.

## S4
Could we give this number a name, for example one day in milliseconds? It would be easier to read and to change later.

## S5
Nice and clean function, thanks! The two tests are good. I suggest one more test with a negative value.
