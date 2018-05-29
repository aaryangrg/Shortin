# Design Choices

## Removing relational fields (manyToMany, ForeignKey) etc. and replacing with ArrayField(char ...)
While it may be more logically appropriate to use relational fields, to capture information
when it comes to such relations, this increases the overhead of every API call as it is more complex
and carries more data than necessary. Hence, the decision was made to sacrifice some extent of ease
of usage to minimize how expensive every API call will be. 

## Duplicating subsets of information in Cache Fields
Again, with the principle aim of reducing the number of API calls required, due to the expensive
nature of this operation, cache fields have been created to store small chunks of information that
may be repeatedly used, but may not warrant a full API call.
E.g. party name cache fields in User.models