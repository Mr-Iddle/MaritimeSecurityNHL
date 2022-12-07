# MaritimeSecurityNHL
Repository for the Assignment AIS/Honeypot. The team's task is to combine previous projects: *Honeynet* and *AIS Encoder/Decoder* to create a system that will provide charting and information display. That will allow users to have a good overview, what is happening when the intruder tries to break in. The overall goal is to educate and spread awareness about the risks in the Maritime cybersecurity field.


## Coding Conventios:
In this document we will clarify and aggree on the structural and naming norms that our code needs to match.

### Indenting
Each new line of code needs to be indented by 2 or more spaces
```
  if(statement){
    code;
}
```

In addition, nested code needs to be indented with 1 space to the prior line

```
for(object name in list){
  for(object name2 in list){
    do something;
    }
  }
```

### Naming
All the naming of classes, methods and variables need to follow the camel casing.
An exception is of course the naming of classes, which start with capital letters

```java
class ChartPlotter,
function readLine(){}
private isValid;
```

### Commenting
Commenting is mandatory for every member and those has to be clearly stated for everyone.
Every function and class needs sane comments to provide a good understanding of the functionality.

### Working with code from others
If code raises questions or the reader does not agree with the input of the code, then a change of code can be requested and it has to be approved by the team/author of the code.
