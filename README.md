# An LSTM approach to Predict Migration based on Google Trends

Code by Nicolas Golenvaux & Pablo Gonzalez Alvarez.

This repository contains the companion codes for the paper
[An LSTM approach to Predict Migration based on Google Trends](https://) by Nicolas Golenvaux, Pablo Gonzalez Alvarez, Harold Silvère Kiossou, Pierre Schaus.

This paper is part of our joint master's thesis work.

## Structure

Files without a comment have a descriptive name to understand what they contain:

    /                                       I am (G)root!
        extract_gti.py
        LICENSE.md                          MIT License
        migration-gti-lstm.ipynb            Notebook to build models
        README.md                           You are here
        data/
            destination_countries.csv   
            LICENSE.md                      CC-BY-4.0 License
            keywords.csv
            origin_countries.csv


## License

Except stated otherwise (cf. [Credits](#credits)), the content of this repository itself as well as the data are licensed under the [Creative Commons Attribution 4.0 International License (CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/), and the  source codes are licensed under the [MIT License](https://spdx.org/licenses/MIT.html).

## Credits:

	Data sources:
        Google Trends (https://www.google.com/trends)
        OECD International Migration Database (https://www.oecd-ilibrary.org/content/data/data-00342-en)
        United Nations Department of Economic and Social Affairs Population Division UN DESA. International Migrant Stock 2019 (https://www.un.org/en/development/desa/population/index.asp)
        World Bank 2020 World Development Indicators (https://datacatalog.worldbank.org/dataset/world-development-indicators)

    Software licenses:
        Keras (https://keras.io) - MIT License
        Matplotlib (https://matplotlib.org/) - Matplotlib License
        NumPy (https://numpy.org/) - BSD-3-Clause License
        Pandas (https://pandas.pydata.org/) - BSD-3-Clause License
        pytrends (https://github.com/GeneralMills/pytrends) -  Apache-2.0 License
        Scikit-learn (https://scikit-learn.org/) - BSD-3-Clause License
        Seaborn (https://seaborn.pydata.org) - BSD-3-Clause License
        Tensorflow (https://www.tensorflow.org) - Apache License 2.0
