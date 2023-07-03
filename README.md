# SODA Checks development example with Test-Driven-Development

In this repository, you will find an example of how to develop a SODA Check using Test-Driven-Development.

In order to do this, we will imagine that we want to validate the dataset output of one of our processes.
This dataset contains metrics of different countries, as you can see the table below.

### Example: Metrics Dataset of Countries
| Metric                                   | Brief Description                                    | Range       | Unit   |
|-----------------------------------------|------------------------------------------------------|-------------|--------|
| Gross Domestic Product (GDP)             | Total value of goods and services produced           | Variable    | dolars |
| Unemployment Rate                        | Percentage of unemployed individuals                 | 0-100       | %      |
| Gini Index                               | Measure of income inequality                         | 0-1         | -      |
| Life Expectancy                          | Average age at which people live                     | Variable    | years  |
| Corruption Perception Index              | Measure of corruption perception                     | 0-100       | -      |

So, we are going to use SODA to validate this dataset, and we will do it using Test-Driven-Development.
Why TDD?
Because we want to be sure that our SODA Checks:
* work properly at development time
* work properly in the future
* are maintainable by other people
* teach us how is validated our dataset
* notify us when our validations don't work by changes in checks definitions
* are being designed simple and easy to understand

