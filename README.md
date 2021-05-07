# event-tuple

# Challenge 5
## Making EventTuple general

There are several ways to use EventTuple() instead of 2 different classes.
First, we can have UserClickedOnButtonEvent and UserLongPressedEvent class instances in EventTuple, so in EventTuple we will be able to determine which class constructor to call, in this case after calling a certain method, for example event_id(), the corresponding UserClickedOnButtonEvent or UserLongPressedEvent class object's method will be called.

Another way is to have one general EventTuple class, with union methods from both classes.
Inside EventTuple's constructor the passed arguments can be stored as fields by storing the information inside __dict__ of the class (vars() returns __dict__), like the following to keep the instances.
```
vars().update(dictionary_of_fields_given_as_an_argument_to_the_constructor) 
```

In that way now we have EventTuple class object with the fields developer passed to the constructor.

