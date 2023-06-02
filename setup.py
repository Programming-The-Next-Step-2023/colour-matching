from setuptools import setup

setup(
    name='squaregame',
    version='1.0.0',
    author='Tara Zohrevand',
    author_email='tarazohrevand@gmail.com',
    description='Squares All Around is an engaging game with seven levels of increasing difficulty. '
                'Players must identify a unique square among four squares with varying widths. '
                'With every three consecutive correct guesses, players advance to the next level. '
                'Level 7 presents the ultimate challenge, offering endless variations in square widths. '
                'Test your visual perception, make accurate guesses, and strive for the highest score '
                'in Squares All Around!',
    packages=['squaregame'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=['pygame']
)

