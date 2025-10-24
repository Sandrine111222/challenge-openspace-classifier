# OpenSpace Organizer
[![forthebadge made-with-python] (https://www.google.com/url?sa=i&url=https%3A%2F%2Fsailendra.hashnode.dev%2Fpython-and-tkinter-mini-project-oddeven&psig=AOvVaw1QXyEq2-_2czviNz2EpfVp&ust=1761391457355000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCNC__dfcvJADFQAAAAAdAAAAABAE)]


## 🏢 Description

Your company moved to a new office at CEVI Ghent. Its an openspace with 6 tables of 4 seats. As many of you are new colleagues, you come up with the idea of changing seats everyday and get to know each other better by working side by side with your new colleagues. 

This script runs everyday to re-assign everybody to a new seat.

[![forthebadge made-with-python] (https://robbreport.com/wp-content/uploads/2023/03/Shapeshifter_Dining.jpg?w=1000)]

## 📦 Repo structure

```
.
├── src/
│   ├── openspace.py
│   ├── table.py
│   └── utils.py
├── .gitignore
├── main.py
├── new_colleagues.csv
├── output.csv
└── README.md
```

## 🛎️ Usage

1. Clone the repository to your local machine.

2 .To run the script, you can execute the `main.py` file from your command line:

```
   python main.py
```

3. The script reads your input file, and organizes your colleagues to random seat assignments. The resulting seating plan is displayed in your console and also saved to an "output.csv" file in your root directory. 

```python
def main():
    input_filepath = "new_colleagues.csv"
    output_filename = "output.csv"

    # Creates a list that contains all the colleagues names
    names = utils.read_names_from_csv(input_filepath)

    # create an OpenSpace()
    open_space = OpenSpace()

    # assign a colleague randomly to a table
    open_space.organize(names)

    # save the seat assigments to a new file
    open_space.store(output_filename)

    # display assignments in the terminal
    open_space.display()

if __name__ == "__main__":
    main()
```
## ⏱️ Timeline

This project took two days for completion.

## 📌 Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 

Connect with me on [https://www.linkedin.com/in/sandrineherbelet?originalSubdomain=be].
