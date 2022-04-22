# Documentation and classes
## Summary
- Document to make the class accessible and easy to understand
- Document before implementing so you can get feedback before writing the code (agile development)
- Inherit from **object()** (done automatically after python 3)
- **Instance variables** for infomration unique to an instance
- **Class variables** for data shared among all instances
- **Regular methods** need "*self*" to use the instance data
- **Class methods** implement alternative constructors. They need "*cls*" so they can create subclass instances as well. Always create alternative constructors where they are desired.
- **Static methods** attach functions to classes. They dont need "*self*" or "*cls*". Static methods imporove discoverability and require context to be specified.
- A **property()** lets getter and setter methods be invoked automattically by attribute access. This allows python classes to expose their instance variables, as you can change the behaviour of dotted acces later.
- The "**__Slots__**" variable implements the *Flyweight Design Pattern* by  suppressing instance dictionaries.