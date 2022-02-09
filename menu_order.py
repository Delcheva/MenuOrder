import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QTabWidget, QLabel, QHBoxLayout, QButtonGroup, QVBoxLayout, \
    QRadioButton, QGroupBox, QPushButton, QGridLayout, QMessageBox

# Set up style sheet for the entire GUI
styles = """
    QWidget{
        background-color: #0099ff;
    }

     QWidget#Tabs{
        background-color: #B7DFEB;
        border-radius: 4px
    }

    QWidget#ImageBorder{
        background-color: #89689c;
        border-width: 2px;
        border-style: solid;
        border-radius: 4px;
        border-color: #66b0ed
    }

    QWidget#Side{
        background-color: #edb366;
        border-radius: 4px
    }

    QLabel{
        background-color: #ed6698;
        border-width: 2px;
        border-style: solid;
        border-radius: 4px;
        border-color: #6693ed
    }

    QLabel#Header{
        background-color: #66ed66;
        border-width: 2px;
        border-style: solid;
        border-radius: 4px;
        border-color: #;
        padding-left: 10px;
        color: #206b20
    }

    QLabel#ImageInfo{
        background-color: #abdaed;
        border-radius: 4px
    }

    QGroupBox{
        background-color: #FCEBCD;
        color: #961A07
    }

    QRadioButton{
        background-color: #c8abeb
    }

    QPushButton{
        background-color: #6924bd;
        border-radius: 4px;
        padding: 6px;
        color: #FFFFFF
    }

    QPushButton:pressed{
        background-color: #f4f5b0;
        border-radius: 4px;
        padding: 6px;
        color: #71ab93
    }
"""


class MenuOrder(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setMinimumSize(600, 700)
        self.setWindowTitle('Food Order')
        self.tabs_and_layout()
        self.show()

    def tabs_and_layout(self):
        """
        Set up tab bar and different tab widgets.
        Also, create the side widget to display items selected.
        """
        self.tab_bar = QTabWidget()

        self.banitsa_tab = QWidget()
        self.banitsa_tab.setObjectName("Tabs")

        self.sushi_tab = QWidget()
        self.sushi_tab.setObjectName("Tabs")

        self.tab_bar.addTab(self.banitsa_tab, "Banitsa")
        self.tab_bar.addTab(self.sushi_tab, "Sushi")

        self.banitsaTab()
        self.sushiTab()

        # Set up side widget which is not part of the tab widget
        self.side_wid = QWidget()
        self.side_wid.setObjectName("Tabs")

        order = QLabel("YOUR ORDER")
        order.setObjectName("Header")

        items_box = QWidget()
        items_box.setObjectName("Side")
        banitsa_label = QLabel("Banitsa Type: ")
        self.display_banitsa = QLabel("")
        ingredients_label = QLabel("Ingredients: ")
        self.display_ingredients = QLabel("")
        extra_label = QLabel("Extra: ")
        self.display_sushi = QLabel("")

        # Set grid layout for objects in side widget
        items_grid = QGridLayout()
        items_grid.addWidget(banitsa_label, 0, 0, Qt.AlignRight)
        items_grid.addWidget(self.display_banitsa, 0, 1)
        items_grid.addWidget(ingredients_label, 1, 0, Qt.AlignRight)
        items_grid.addWidget(self.display_ingredients, 1, 1)
        items_grid.addWidget(extra_label, 2, 0, Qt.AlignRight)
        items_grid.addWidget(self.display_sushi, 2, 1)
        items_box.setLayout(items_grid)

        # Set main layout for side widget
        f_box = QVBoxLayout()
        f_box.addWidget(order)
        f_box.addWidget(items_box)
        f_box.addStretch()
        self.side_wid.setLayout(f_box)

        # Add widgets to main window and set layout
        v_box = QHBoxLayout()
        v_box.addWidget(self.tab_bar)
        v_box.addWidget(self.side_wid)
        self.setLayout(v_box)

    def banitsaTab(self):
        """
        Create the pizza tab. Allows the user to select the type
        of pizza and topping using radio buttons.
        """
        tab_banitsa = QLabel("Build your own Banitsa")
        tab_banitsa.setObjectName("Header")

        desc_box = QWidget()
        desc_box.setObjectName("ImageBorder")

        banitsa_image_path = "images/banitsa.png"
        banitsa_image = self.loading_image(banitsa_image_path)

        banitsa_desc = QLabel()
        banitsa_desc.setObjectName("ImageInfo")

        banitsa_desc.setText("Build a custom Banitsa for you. Start with your favorite pie crust, " 
                             "and the perfect amount of cheese and other ingredients.")
        banitsa_desc.setWordWrap(True)

        h_box = QHBoxLayout()
        h_box.addWidget(banitsa_image)
        h_box.addWidget(banitsa_desc)

        desc_box.setLayout(h_box)

        crust_box = QGroupBox()
        crust_box.setTitle("Choose your Pie Crust")

        self.crust_group = QButtonGroup()
        b_box = QVBoxLayout()
        crust_list = ["Ground Crusts", "Finely Ground Crusts", "Whole Grain Crusts"]

        for cr in crust_list:
            crust_rb = QRadioButton(cr)
            b_box.addWidget(crust_rb)
            self.crust_group.addButton(crust_rb)

        crust_box.setLayout(b_box)

        # Create group box that will contain toppings choices
        ingredients_box = QGroupBox()
        ingredients_box.setTitle("Choose your Ingredients")

        # Set up button group for toppings radio buttons
        self.ingredients_group = QButtonGroup()
        b_box = QVBoxLayout()

        ingredients_list = ["Yellow cheese", "Sausage", "Bacon",
                            "Spinach", "Mushroom", "Onion",
                            "Red Pepper", "Tomato", "Cheese"]
        # Create radio buttons for the different toppings and
        # add to layout
        for top in ingredients_list:
            ingredients_b = QRadioButton(top)
            b_box.addWidget(ingredients_b)
            self.ingredients_group.addButton(ingredients_b)
            self.ingredients_group.setExclusive(False)

        ingredients_box.setLayout(b_box)

        # Create button to add information to side widget
        # when clicked
        add_order_button1 = QPushButton("Add To Order")
        add_order_button1.clicked.connect(self.displayBanitsaInOrder)

        # create layout for pizza tab (page 1)
        page1_v_box = QVBoxLayout()
        page1_v_box.addWidget(tab_banitsa)
        page1_v_box.addWidget(desc_box)
        page1_v_box.addWidget(crust_box)
        page1_v_box.addWidget(ingredients_box)
        page1_v_box.addStretch()
        page1_v_box.addWidget(add_order_button1, alignment=Qt.AlignRight)

        self.banitsa_tab.setLayout(page1_v_box)

    def sushiTab(self):
        """
        Set up widgets and layouts to display information to the user about the page
        """
        tab_sushi = QLabel("Try the perfect Sushi!")
        tab_sushi.setObjectName("Header")
        descr_box = QWidget()
        descr_box.setObjectName("ImageBorder")
        sushi_image_path = "images/sushi.jpeg"
        sushi_image = self.loading_image(sushi_image_path)
        sushi_desc = QLabel()
        sushi_desc.setObjectName("ImageInfo")
        sushi_desc.setText("One box of 12 pieces of perfectly made sushi wrapped with love for you.")
        sushi_desc.setWordWrap(True)

        h_box = QHBoxLayout()
        h_box.addWidget(sushi_image)
        h_box.addWidget(sushi_desc)

        descr_box.setLayout(h_box)

        sushi_box = QGroupBox()
        sushi_box.setTitle("Choose your Flavor")

        self.sushi_group = QButtonGroup()
        b_box = QVBoxLayout()
        sushi_list = ["Sashimi", "Maki", "Uramaki", "Temaki", "Hosomaki"]

        for fl in sushi_list:
            flavor_rb = QRadioButton(fl)
            b_box.addWidget(flavor_rb)
            self.sushi_group.addButton(flavor_rb)

        sushi_box.setLayout(b_box)

        add_order_button2 = QPushButton("Add To Order")
        add_order_button2.clicked.connect(self.displaySushiInOrder)

        page2_v_box = QVBoxLayout()
        page2_v_box.addWidget(tab_sushi)
        page2_v_box.addWidget(descr_box)
        page2_v_box.addWidget(sushi_box)
        page2_v_box.addWidget(add_order_button2, alignment=Qt.AlignRight)
        page2_v_box.addStretch()

        self.sushi_tab.setLayout(page2_v_box)

    def collectIngredientsInList(self):
        """
        Create list of all checked toppings radio  buttons.
        """
        return [button.text() for i, button in enumerate(self.ingredients_group.buttons()) if button.isChecked()]

    def displayBanitsaInOrder(self):
        """
        Collect the text from the radio buttons that are checked on pizza page.
        Display text in side widget.
        """
        try:
            banitsa_text = self.crust_group.checkedButton().text()
            self.display_banitsa.setText(banitsa_text)

            ingredients = self.collectTopingsInList()
            ingredients_str = '\n'.join(ingredients)
            self.display_ingredients.setText(ingredients_str)
            self.repaint()
        except AttributeError:
            print("No value selected.")
            QMessageBox.warning(self, "Error", "No value selected", QMessageBox.Ok)
            pass

    def displaySushiInOrder(self):
        """
        Collect the text from the radio buttons that are checked on wings page.
        Display text in side widget.
        """
        try:
            text = self.sushi_group.checkedButton().text() + " Sushi"
            self.display_sushi.setText(text)
            self.repaint()
        except AttributeError:
            print("No value selected.")
            QMessageBox.warning(self, "Error", "No value selected", QMessageBox.Ok)
            pass

    def loading_image(self, path):
        """
        Load and scale images.
        :param path: path to the file
        """
        try:
            with open(path):
                image = QLabel(self)
                image.setObjectName("ImageInfo")
                pixmap = QPixmap(path)
                image.setPixmap(pixmap.scaled(image.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
                return image
        except FileNotFoundError:
            print("Image not found.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
     # add styles
    app.setStyleSheet(styles)
    window = MenuOrder()
    sys.exit(app.exec_())
