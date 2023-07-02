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



## 🧑‍🏭 Setup

> [Pyenv](https://www.wolfremium.dev/blog/python-multiple-versions) >
> [Makefile](https://hernandis.me/2017/03/20/como-hacer-un-makefile.html)

After `pyenv` installation, run this in this directory:

```bash
pyenv install 3.10.9
```

Set default Python version for current directory:

```bash
pyenv local 3.10.9
```

Basic setup to use pipenv.

```bash
python -m pip install -U pip && pip install pipenv
```

This project includes make commands to make your life easier.

```bash
sudo apt-get install make
```

Install all the dependencies, and generates a virtual environment.

```bash
make setup
```

## 🧑‍💻 Commands

Run `make help` to see all available commands.

## 📚 Testing libraries

- [UnitTest](https://docs.python.org/3/library/unittest.html)
- [Pytest](https://docs.pytest.org/en/7.1.x/getting-started.html#get-started)
- [Hypothesis](https://hypothesis.readthedocs.io/en/latest/quickstart.html)
- [Intro to property-based testing in Python](https://www.freecodecamp.org/news/intro-to-property-based-testing-in-python-6321e0c2f8b/)

## 💩 Troubleshooting

- [Select VSCode Interpreter (modules not found after installation)](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment)
