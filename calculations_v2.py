"""
### Work in progress!!!!

## Calculations and processes v2

Same program:
    Slightly Faster.
    More Scalable.
    Better Designed.
    Tons of Features.


An Object Oriented implementation of the 'calculations & processes v1'.

Mathematical Calculations:
    Arithmetic Calculations
    Round Decimal Values
    Square Root Calculations
    Square Root in-range
    Factorial Calculator
    Factorials in-range
    Find Minimum and Maximum numbers from a list
    Find Even or Odd
    Even or Odd in-range
    Find Leap Year
    Leap Years in-range
    Fibonacci Series
    Prime numbers

Conversions:
    Temperature Conversion
    Number systems Conversion
    Data Storage Conversion

Generators:
    Hash Generation.
    Pattern Generation.
    Random Numbers Generation.
    Password Generation.


Find
Area Calculations
String Manipulation


"""


import sys
import math
import random
import hashlib as hl
import secrets
from string import ascii_letters, punctuation, digits


class Helper:
    """
    ### Helper Methods.
    Contains methods to help in general tasks.

    """

    def __init__(self) -> None:
        ...

    def get_int(self, prompt="Enter Int (ctrl+c to quit): ", only_positive=False):
        """Takes a valid 'int' input from user"""

        while True:
            try:
                i = int(input(prompt).strip())
                if only_positive and i < 0:
                    continue
                return i

            except ValueError:
                print("Invalid: only integers accepted!\n")
            except KeyboardInterrupt:
                sys.exit(0)

    def get_float(self, prompt="Enter Float (ctrl+c to quit): "):
        """Takes a valid 'float' input from user"""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid: only floats accepted!\n")
            except KeyboardInterrupt:
                sys.exit(0)

    def get_string(self, prompt="Enter String (ctrl+c to quit): "):
        """Takes a valid 'str' input from user"""
        try:
            return input(prompt).strip()
        except KeyboardInterrupt:
            sys.exit(0)


class Maths:
    """
    ## Mathematical Methods
    Base class for mathematical methods"""

    def __init__(self) -> None:
        # Defining REGEX Patterns
        ...

    def arithmetic(self, expression):
        """
        #### Arithmetical calculations
        Calculates the Arithmetic Expressions

        Supported Operators:
            - Addition: +
            - Subtraction: -
            - Multiplication: *
            - Division: /
            - Modulus: %
            - Floor division: //
            - Exponent: **

        ```
        # Example:
        >> expression = '5+5-5*5/5'
        >> math.arithmetic(expression)
        5.0
        ```
        """

        try:
            return eval(expression)
        except (NameError, SyntaxError):
            raise ValueError

    def round_off(self, f=3.141592, precision=2):
        """
        #### Round numbers
        Rounds `f` using `precision`.

        ```
        >> f = 3.141592
        >> precision = 2
        >> math.round_off(f, precision)
        3.14
        ```
        """

        return round(f, precision)

    def square_root(self, value=9):
        """
        #### Square root
        Find the square root of a `value`.

        ```
        # Example:
        >> value = 9
        >> math.square_root(value)
        3.0
        ```
        """
        return round(math.sqrt(value), 4)

    def square_root_inrange(self, f=1, t=5):
        """
        #### Square roots in-range
        Returns a dictionary of Square roots of all numbers in a given range,
        where keys are numbers and values are their square roots.

        ```
        # Example:
        >> f = 1
        >> t = 5
        >> math.square_root_inrange(f, t)


        ```
        """
        roots = {}

        # Calculating the square roots
        for i in range(f, t+1):
            roots[f"{i}"] = round(math.sqrt(i), 3)

        # Return the square roots
        return roots

    def fact(self, value=4):
        """
        #### Factorials
        Finds the factorial of `value`

        ```
        # Example:
        >> value = 4
        >> math.fact(value)
        24
        ```
        """

        # Calculate & return the factorial
        return math.factorial(value)

    def fact_inrange(self, f=1, t=5):
        """
        #### Factorials in-range
        Returns a dictionary of factorial of all numbers in given range, where 
        keys are the numbers and values are their factorials.

        ##### Note: factorials grow exponentially. avoid giving a range larger than 20 numbers.

        ```
        # Example:
        >> f = 1
        >> t = 5
        >> math.fact_inrange(f, t)
        {
            '1': 1, '2': 2,
            '3': 6, '4': 24,
            '5': 120
        }
        ```
        """

        factorials = {}
        # Calculating the factorials
        for i in range(f, t+1):
            # factorials.append(math.factorial(i))
            factorials[f"{i}"] = math.factorial(i)

        print(factorials)

    def min_max(self, values=[1, 5, 10, 52, 0]):
        """
        #### Minimum / Maximum numbers
        Finds the minimum and maximum numbers within a list.

        Returns a tuple e.g. (min, max)

        ```
        # Example:
        >> values = [1,5,10,52,0]
        >> math.min_max(values)
        (0, 52)
        ```

        """
        return (min(values), max(values))

    def even_odd(self, n=5):
        """
        #### Even / Odd
        Checks if `n` is even or not.
        Returns a <bool>
            - True == 'Even'
            - False == 'Odd'

        ```
        # Example:
        >> n = 5
        >> math.even(n)
        True
        ```
        """

        return True if n % 2 == 0 else False

    def even_odd_inrange(self, f=1, t=10):
        """
        #### Even / Odd in-range
        Finds all even and odd numbers in a given range.

        Returns a dictionary with `'even'` key containing even numbers and 
        `'odd'` key containing odd numbers.

        ```
        >> f = 1
        >> t = 10
        >> math.even_odd_inrange(f, t)
        {
            'even': [2, 4, 6, 8, 10],
            'odd': [1, 3, 5, 7, 9]
        }
        ```
        """
        master = {'even': [], 'odd': []}

        for i in range(f, t+1):
            # one liner: if even throw in 'even', if odd throw in 'odd'
            master["even"].append(i) if i % 2 == 0 else master["odd"].append(i)

        return master

    def leap_year(self, year=2016):
        """
        #### Leap year
        Checks if `year` is leap year or not

        ```
        # Example:
        >> year = 2016
        >> math.leap_year(year)
        True
        ```
        """

        return True if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) else False

    def leap_year_inrange(self, f=2016, t=2024):
        """
        #### Leap years in-range
        Finds all leap years in range between two years.

        Returns a list of all found leap years.

        ```
        # Example:
        >> f = 2016
        >> t = 2024
        >> math.leap_year_inrange(f,t)
        [2016, 2020, 2024]
        ```
        """

        # Stores all leap years
        years = []

        # Finding leap years
        for year in range(f, t+1):
            if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
                years.append(year)

        return years

    def gcd_lcm(self, a=4, b=5, op="lcm"):
        """
        #### LCM / GCD
        Aplies GCD (Greatest common divisor) or LCM (Least common multiple)
        operations on `a` and `b`

        ```
        # Example:
        >> a = 4
        >> b = 5
        >> op = "lcm"
        >> math.gcd_lcm(a, b, op)
        20
        ```
        """

        match op:
            case "hcf":
                return math.gcd(a, b)
            case "lcm":
                return math.lcm(a, b)
            case _:
                raise TypeError(f"{op} is not an attribute of 'op'")

    def fibonacci_series(self, n=5):
        """
        #### Fibonacci Series.
        A Series in which each number is the sum of two preceeding numbers.

        0 and 1 are always the first two numbers in the series.

        Returns a list of Fibonacci `n` numbers.

        ```
        # Example:
        >> limit = 5
        >> math.fibonacci_series(limit)
        [0, 1, 1, 2, 3]
        ```
        """

        # First two numbers
        a = 0
        b = 1

        # To store the series
        series = [0, 1]

        # Checking if the limit is 1
        if n == 1:
            return [0]

        # Generating the series
        for _ in range(n-2):
            temp = a+b
            a = b
            b = temp

            # Append to series
            series.append(temp)

        # Returning the series
        return series

    def prime_number(self, n=5):
        """
        #### Prime number
        Returns True if `n` is a prime number, False otherwise.

        A Prime number is a number which is divided only by 1 and itself.

        ```
        # Example:
        >> n = 5
        >> math.prime_number(n)
        True
        ```
        """

    # count is {Division count > (how many times it was divided)}
        count = 0

        for i in range(1, n+1):
            if (count > 2):
                break

            if n % i == 0:
                count += 1

        # True if count = 2, False otherwise
        return True if count == 2 else False

    def prime_number_inrange(self, limit=10):
        """
        #### Prime Numbers
        Prime number is a number that is divided only by 1 and itself.

        For example:
            - 5 is a prime number as its factors are 1 and 5.
            - 6 is not a prime number which have factors 1, 2, 3 and 6

        ```
        # Example:
        >> limit = 10
        >> math.prime_number_inrange(limit)
        [2, 3, 5, 7]
        ```
        """

        # Stores all prime numbers
        numbers = []

        for i in range(1, limit + 1):
            # i is {Current number}

            # count is {Division count > (how many times it was divided)}
            count = 0

            for j in range(1, i+1):
                if i % j == 0:
                    count += 1

            # If prime > { if divide count was 2 }
            if count == 2:
                numbers.append(i)

        # Return the numbers list
        return numbers


class Converters:
    """Base class for Conversions methods"""

    def __init__(self) -> None:
        pass

    def temperature_convertor(self, _temp=30.0, unit='cel'):
        """
        #### Converts temperature 

        Just Pass in the `_temp` containing the temperature and its unit in opr.
        Leave the rest to this function.

        Supported Units: opr values
        - cel
        - fah
        - kel

        ```
        # Example:
        >> _temp = 30
        >> unit = "cel"
        >> convertor.temperature_convertor(_temp, unit)
        {'fah':86.0,'kel':303.15}
        ```
        """
        # Master Dictionary
        master = {}

        match unit:
            case 'cel':
                # Celsius to Fahrenheit
                master['fah'] = round((_temp * 1.8) + 32, 3)
                # Celsius to Kelvin.
                master['kel'] = round(_temp + 273.15, 3)

                return master

            case 'fah':
                # Fahrenheit to Celsius.
                master['cel'] = round((_temp-32)*5/9, 3)
                # Fahrenheit to Kelvin.
                master['kel'] = round(((_temp-32)/1.8)+273.15, 3)

                return master

            case 'kel':
                # Kelvin to Fahrenheit.
                master['fah'] = round((((_temp-273.15)*1.8)+32), 3)
                # Kelvin to Celsius.
                master['cel'] = round(_temp - 273.15, 3)

                return master
            case _:
                raise ValueError("Invalid unit: Undefined unit")

    def number_systems_convertor(self, value='11010', unit='bin'):
        """
        #### Converts Number Systems

        Just Pass in the string containing the value and its type in unit.
        Leave the rest to this function.

        Supported opr:
        - bin
        - dec
        - hex
        - oct

        ```
        # Example:
        >> value = '11010'
        >> unit = 'bin'
        >> convertor.number_systems_convertor(value, unit)
        {'dec':26,'hex':'1A','oct':32}
        ```
        """

        # Master Dictionary
        master = {}

        match unit:
            case "bin":
                # Binary conversion: int2 required
                temp = int(value, 2)
                master['dec'] = int(temp)
                master['hex'] = hex(int(temp)).replace("0x", "").upper()
                master['oct'] = oct(int(temp)).replace("0o", "")

                return master

            case "dec":
                # Decimal conversion: int10 required
                temp = int(value)
                master['bin'] = bin(temp).replace("0b", "")
                master['hex'] = hex(temp).replace("0x", "").upper()
                master['oct'] = oct(temp).replace("0o", "")

                return master

            case "hex":
                # Hexadecimal conversion: int16 required
                temp = int(value, 16)
                master['bin'] = bin(temp).replace("0b", "")
                master['dec'] = int(temp)
                master['oct'] = oct(temp).replace("0o", "")

                return master

            case "oct":
                # Octal conversion: int8 required
                temp = int(value, 8)
                master['bin'] = bin(temp).replace("0b", "")
                master['dec'] = int(temp)
                master['hex'] = hex(temp).replace("0x", "").upper()

                return master

            case _:
                raise ValueError("Invalid opr: Undefined Operation")

    def data_storage_convertor(self, value=1.0, unit="kb"):
        """
        #### Converts Data storage units

        Just pass in the `value` and its `unit`, Leave the rest to this function.
        Returns a dictionary containing all supported units converted.

        Supported Units:
        - B = Bytes
        - MB = KiloBytes
        - KB = MegaBytes
        - GB = GigaBytes
        - TB = TeraBytes
        - PB = PetaBytes

        ```
        # Example
        >> values = 1024
        >> unit = "kb"
        >> converter.data_storage_converter(value, unit)
        {"b":1048576,"kb":1024,"mb":1,
        "gb":0.000976562,"tb":0.0000009537,
        "pb":0.0000000009}
        ...
        ```
        """

        # Master Dictionary to store converted values
        master = {}

        # Unit Factors
        factors = {
            "kb": 1024,
            "mb": 1024 ** 2,
            "gb": 1024 ** 3,
            "tb": 1024 ** 4,
            "pb": 1024 ** 5
        }

        # converting input value to bytes
        _bytes = 0.0
        match unit:
            case "kb":
                _bytes = value * factors["kb"]

            case "mb":
                _bytes = value * factors["mb"]

            case "gb":
                _bytes = value * factors["gb"]

            case "tb":
                _bytes = value * factors["tb"]

            case "pb":
                _bytes = value * factors["pb"]

            case _:
                # Default case
                raise ValueError("Invalid unit: undefined unit")

        # Converting bytes to other units
        master["b"] = _bytes
        master["kb"] = _bytes / factors["kb"]
        master["mb"] = _bytes / factors["mb"]
        master["gb"] = _bytes / factors["gb"]
        master["tb"] = _bytes / factors["tb"]
        master["pb"] = _bytes / factors["pb"]

        # returning the dictionary
        return master


class Generators:
    """Base class for generator methods"""

    def __init__(self) -> None:
        pass

    def generate_hash(self, text: str):
        """
        ### Hash Generator/Converter

        Algorithms Available:
        - MD-5
        - SHA-1
        - SHA-224
        - SHA-256
        - SHA-384
        - SHA-512
        - blake-2b
        - blake-2s

        ```
        # Example:
        >> text = "Python is awesome!"
        >> gen.generate_hash(text)
        {
            'md-5': '...','sha-1': '...',
            'sha-224': '...','sha-256': '...', 
            'sha-384': '...','sha-512': '...',
            'blake-2b': '...','blake-2s': '...'
        }
        ```
        """

        master = {}

        # If text isn't encoded, go ahead and encode it!
        if type(text) != bytes:
            text = text.encode()

        # Hashing the text and storing in Master dictionary
        master["md-5"] = hl.md5(text).hexdigest()
        master["sha-1"] = hl.sha1(text).hexdigest()
        master["sha-224"] = hl.sha224(text).hexdigest()
        master["sha-256"] = hl.sha256(text).hexdigest()
        master["sha-384"] = hl.sha384(text).hexdigest()
        master["sha-512"] = hl.sha512(text).hexdigest()
        master["blake-2b"] = hl.blake2b(text).hexdigest()
        master["blake-2s"] = hl.blake2s(text).hexdigest()

        # Returning the dictionary
        return master

    def generate_patterns(self):
        """
        ### Generate Patterns
        Generates patterns of sorts [coming soon!]
        """
        ...

    def generate_random_numbers(self, n: int, from_: int, to: int):
        """
        ### Random Numbers Generator
        returns a generator of `n` random numbers
        """

        # 'n' must be greater than 0
        if n <= 0:
            return None

        # 'to' must be greater than 'from_'
        if to <= from_:
            raise ValueError("'to' must be greater than 'from_'")

        # generating random numbers
        for _ in range(n):
            yield random.randrange(from_, to)

    def generate_password(self, n: int, length: int):
        """
        ### Random Password Generation
        returns a generator of `n` randomly generated passwords of length `length`
        """
        # 'n' must be greater than zero
        if not n > 0:
            raise ValueError("'n' must be greater than zero")

        # 'length' must be greater than zero
        if not length > 0:
            raise ValueError("'length' must be greater than zero")

        # characters to use to generate passwords
        characters = ascii_letters + digits + punctuation

        # generating password
        for _ in range(n):
            password = ""
            for i in range(length):
                password += secrets.choice(characters)

            yield password


class Finders:
    """Base class for finder methods"""

    ...


class Calculations:
    """Base class for area calculation methods"""

    ...


class Strings:
    """Base class for string manipulations methods"""

    ...


# ! REMOVE
m = Maths()

print(m.prime_number(int(input("Enter num: "))))
