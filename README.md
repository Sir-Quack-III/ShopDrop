# ShopDrop

An esolang created for truttle1's esojam

## Documentation
In shopdrop, you are a car that can load and empty produce into numerous houses.

A shopdrop file is comprised of three parts:
    - Shopping list
    - route
    - map

The shopping list is a JSON object that contains the food you are going to collect. Think of it as constants that you cannot change.

The route section is optional, but easier to program in. The route tells the car exactly where to go. The route, however, cannot contain control flow.

The map section is where the car can drive. The car is a `=` character, and will travel to the right forever by default when the program runs.

### Shopping list
There are numerous types of produce you can put on your shopping list, all of which have specific uses.

Onions are used to store character data. For example, this is the shopping list to get an 'A' character:
```
1:{
    "onion":65
}
```

### Map
This is an example map:
```
   @  %
=--l--e--.
```
Lets go through this. Your car is the `=` character. By default your car will begin going right. Your car can only stay on road characters, which are `-`,`+`, and `|`.

When your car arrives at the `l` character, it receives the command to load something into its trunk. Your car will search for the closest grocery store (the `@`) to load from. It finds the grocery store right above it, and starts loading groceries from the first shopping list (see above) into its trunk. We now have 65 onions in our car. The next time it loads, it will load from the second shopping list, etc. When it is done loading, it will continue going forward.

When your car reaches the `e` character, it receives the command to empty all contents from its trunk into the closest house. The closest house is `%` (the outhouse), which is a special house that prints whatever is emptied into it. We then empty our 65 onions into the outhouse. Because onions are characters, the outhouse prints the ascii value for 65: `A`.

Your car then continues driving until it reaches the `.`, which tells the car to stop driving, ending the program.

(If you noticed that the `-` characters are redundant than you are correct, the more concise program would be:
```
 @%
=le.
```
)