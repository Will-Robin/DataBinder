# DataBinder

This project aims to interface experimental conditions and data with models
designed to describe them.

One of the key processes in modelling is to make sure that the model is designed
within the parameters of the data it is designed to model. For example, does the
model contain the variables given in the data? Does the model cover the correct
time period for a time series? Is the model compatible with the data?

These questions are rather mechanical: once the model has been selected, and the
data specified, it is trivial to make sure that they are compatible.

This package aims to provide a framework for 'binding' data and models so that
a complete and valid model can be compiled from both of them as output.
