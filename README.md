# ShopDrop

An esolang created for truttle1's esojam

## Documentation
In shopdrop, you are a car that can load and empty produce into numerous houses.

A shopdrop file is comprised of two parts:
    - Shopping list
    - map

The shopping list is a JSON object that contains the food you are going to collect. Think of it as constants that you cannot change.

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
=  l  e.
```
Lets go through this. Your car is the `=` character. By default your car will begin going right.

When your car arrives at the `l` character, it receives the command to load something into its trunk. Your car will search for the closest grocery store (the `@`) to load from. It finds the grocery store right above it, and starts loading groceries from the first shopping list (see above) into its trunk. We now have 65 onions in our car. The next time it loads, it will load from the second shopping list, etc. When it is done loading, it will continue going forward.

When your car reaches the `e` character, it receives the command to empty all contents from its trunk into the closest house. The closest house is `%` (the outhouse), which is a special house that prints whatever is emptied into it. We then empty our 65 onions into the outhouse. Because onions are characters, the outhouse prints the ascii value for 65: `A`.

Your car then continues driving until it reaches the `.`, which tells the car to stop driving, ending the program.

(If you noticed that the space characters are redundant than you are correct, the more concise program would be:
```
 @%
=le.
```
)

#### Other commands
Im writing this like a week after all the previous shit so idkddkkirhgniuesgdfd

The `d` command duplicates the first thing in your shopping list. I added this like two seconds ago because I realized I couldnt do loops

The `c` command clears everything in your car

#### Variables
Variables are houses. Houses can be one of the following characters:
```
$,#,+,-
```
`$` is a house that only has onions in it.
`#` is a house that only has potatoes in it.
wait shit i forgot to explain potatoes
potatoes are numbers
`+` is a house that adds the number of potatoes in it
`-` is a house that subtraxts the number of potatoes in it




### Directions
So im an idiot and made two commands for directions: someonetgfing that changes your car direction and another one that changes it as long as everything in your trunk is zero but no thats different to haveing an empty trunk you actually have to go to the store and order zero potatoes or something so if everything is zero than the car changes directions

now the first command for changing directions makes since but the other one is just numbers which is just about the most useless thing you could ever think of but heeere is a guide:::
```
0:right
1:down
2: left
3:up
```
ok so if your car goes onto a "3" character than it will go up if everything in your trunk is zero

ok

now if your car lands on `^ or > or < or v` than it will go the direction the error is pointing its very sepreprlerpgflrepglrepgkfrighfjwoei as you can see

i think thats the entire language yeah