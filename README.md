# Invoice Generator
## Description
The Invoice Generator is a Python script that automates the creation of invoices in Microsoft Word format using a graphical user interface (GUI) built with ```tkinter```. It allows users to enter customer details, add items to the invoice with their quantities and prices, and then generates a formatted invoice in a Word document. The script also provides the functionality to save the generated invoice in the same directory as the Python file.

## Features
```User-friendly GUI```: The script provides an intuitive graphical interface for users to enter customer details and add items to the invoice.

```Invoice Generation```: Upon entering customer information and adding items to the invoice, the script generates a formatted invoice with a subtotal, sales tax, and total.

```Data Validation```: The script includes basic data validation to ensure that users enter valid inputs, such as non-empty descriptions and positive prices.

```Auto-Naming of Invoices```: Each generated invoice is automatically named using the customer's name and the current date and time to avoid overwriting previous invoices.

```File Saving```: The script saves the generated invoice as a Word document in the same directory as the Python file.

## Prerequisites
```Python 3.x ```: Make sure you have Python 3.x installed on your system. You can download Python from the official website: https://www.python.org/downloads/

```Required Packages```: The script depends on two Python packages: **tkinter** and **docxtpl**. These packages handle the GUI and Word document generation, respectively. Install the required packages using the following command:
```
pip install tk docxtpl
```

```Invoice Template```: The script assumes the presence of an "invoice_template.docx" file in the same directory. This Word document serves as the template for generating invoices. You can customize the template to match your business's branding and layout.

## Usage
Clone the repository or download the Python script and the "invoice_template.docx" file to a directory of your choice.

Open a terminal or command prompt and navigate to the directory containing the Python script and the ```invoice_template.docx``` file.

**Run the script using the following command:**


```python invoice_generator.py```

The Invoice Generator GUI will appear. Enter the customer's first name, last name, and phone number. Then, add items to the invoice by specifying the quantity, description, and unit price and clicking the "Add Item" button.

After adding all the items, click the "Generate Invoice" button to create the invoice. The generated invoice will be saved in the same directory as the Python file with a name formatted as "new_invoice_customername_date-time.docx".

To create a new invoice, click the ```New Invoice``` button. It will clear the form, allowing you to enter details for a new customer and create a new invoice.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
The Invoice Generator script is inspired by the need for an efficient and automated way to create invoices for small businesses. It uses the tkinter library for GUI and docxtpl for generating Word documents from templates.

## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to create an issue or submit a pull request