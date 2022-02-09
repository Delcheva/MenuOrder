


    def setupTabsAndLayout(self):
        """
        Set up tab bar and different tab widgets.
        Also, create the side widget to display items selected.
        """
        self.tab_bar = QTabWidget()

        self.pizza_tab = QWidget()
        self.pizza_tab.setObjectName("Tabs")

        self.wings_tab = QWidget()
        self.wings_tab.setObjectName("Tabs")

        self.tab_bar.addTab(self.pizza_tab, "Pizza")
        self.tab_bar.addTab(self.wings_tab, "Wings")

        self.pizzaTab()
        self.wingsTab()

        # Set up side widget which is not part of the tab widget
        self.side_widget = QWidget()
        self.side_widget.setObjectName("Tabs")

        order_label = QLabel("YOUR ORDER")
        order_label.setObjectName("Header")

        items_box = QWidget()
        items_box.setObjectName("Side")
        pizza_label = QLabel("Pizza Type: ")
        self.display_pizza_label = QLabel("")
        toppings_label = QLabel("Toppings: ")
        self.display_toppings_label = QLabel("")
        extra_label = QLabel("Extra: ")
        self.display_wings_label = QLabel("")

        # Set grid layout for objects in side widget
        items_grid = QGridLayout()
        items_grid.addWidget(pizza_label, 0, 0, Qt.AlignRight)
        items_grid.addWidget(self.display_pizza_label, 0, 1)
        items_grid.addWidget(toppings_label, 1, 0, Qt.AlignRight)
        items_grid.addWidget(self.display_toppings_label, 1, 1)
        items_grid.addWidget(extra_label, 2, 0, Qt.AlignRight)
        items_grid.addWidget(self.display_wings_label, 2, 1)
        items_box.setLayout(items_grid)

        # Set main layout for side widget
        side_v_box = QVBoxLayout()
        side_v_box.addWidget(order_label)
        side_v_box.addWidget(items_box)
        side_v_box.addStretch()
        self.side_widget.setLayout(side_v_box)

        # Add widgets to main window and set layout
        main_h_box = QHBoxLayout()
        main_h_box.addWidget(self.tab_bar)
        main_h_box.addWidget(self.side_widget)
        self.setLayout(main_h_box)

    def pizzaTab(self):
        """
        Create the pizza tab. Allows the user to select the type
        of pizza and topping using radio buttons.
        """
        tab_pizza_label = QLabel("BUILD YOUR OWN PIZZA")
        tab_pizza_label.setObjectName("Header")

        description_box = QWidget()
        description_box.setObjectName("ImageBorder")

        pizza_image_path = "images/4.jpg"
        pizza_image = self.loadImage(pizza_image_path)

        pizza_desc = QLabel()
        pizza_desc.setObjectName("ImageInfo")

        pizza_desc.setText("Build a custom pizza for you. Start with your favorite crust and add any toppings, "
                           "plus the perfect amount of cheese and sauce.")
        pizza_desc.setWordWrap(True)

        h_box = QHBoxLayout()
        h_box.addWidget(pizza_image)
        h_box.addWidget(pizza_desc)

        description_box.setLayout(h_box)

        crust_gbox = QGroupBox()
        crust_gbox.setTitle("CHOOSE YOUR CRUST")

        self.crust_group = QButtonGroup()
        gb_v_box = QVBoxLayout()
        crust_list = ["Hand-Tossed", "Flat", "Stuffed"]

        for cr in crust_list:
            crust_rb = QRadioButton(cr)
            gb_v_box.addWidget(crust_rb)
            self.crust_group.addButton(crust_rb)

        crust_gbox.setLayout(gb_v_box)

        # Create group box that will contain toppings choices
        toppings_gbox = QGroupBox()
        toppings_gbox.setTitle("CHOOSE YOUR TOPPINGS")

        # Set up button group for toppings radio buttons
        self.toppings_group = QButtonGroup()
        gb_v_box = QVBoxLayout()

        toppings_list = ["Pepperoni", "Sausage", "Bacon", "Canadian Bacon",
                         "Beef", "Mushroom", "Onion",
                         "Olive", "Green Pepper", "Tomato", "Spinach", "Cheese"]
        # Create radio buttons for the different toppings and
        # add to layout
        for top in toppings_list:
            toppings_rb = QRadioButton(top)
            gb_v_box.addWidget(toppings_rb)
            self.toppings_group.addButton(toppings_rb)
        self.toppings_group.setExclusive(False)

        toppings_gbox.setLayout(gb_v_box)

        # Create button to add information to side widget
        # when clicked
        add_to_order_button1 = QPushButton("Add To Order")
        add_to_order_button1.clicked.connect(self.displayPizzaInOrder)

        # create layout for pizza tab (page 1)
        page1_v_box = QVBoxLayout()
        page1_v_box.addWidget(tab_pizza_label)
        page1_v_box.addWidget(description_box)
        page1_v_box.addWidget(crust_gbox)
        page1_v_box.addWidget(toppings_gbox)
        page1_v_box.addStretch()
        page1_v_box.addWidget(add_to_order_button1, alignment=Qt.AlignRight)

        self.pizza_tab.setLayout(page1_v_box)

    def wingsTab(self):
        """
        Set up widgets and layouts to display information to the user about the page
        """
        tab_wings_label = QLabel("TRY OUR AMAZING WINGS")
        tab_wings_label.setObjectName("Header")
        description_box = QWidget()
        description_box.setObjectName("ImageBorder")
        wings_image_path = "images/5.png"
        wings_image = self.loadImage(wings_image_path)
        wings_desc = QLabel()
        wings_desc.setObjectName("ImageInfo")
        wings_desc.setText("6 pieces of rich-tasting, white meat chicken that will have you coming back for more.")
        wings_desc.setWordWrap(True)

        h_box = QHBoxLayout()
        h_box.addWidget(wings_image)
        h_box.addWidget(wings_desc)

        description_box.setLayout(h_box)

        wings_gbox = QGroupBox()
        wings_gbox.setTitle("CHOOSE YOUR FLAVOR")

        self.wings_group = QButtonGroup()
        gb_v_box = QVBoxLayout()
        wings_list = ["Buffalo", "Sweet-Sour", "Teriyaki", "Barbecue"]

        for fl in wings_list:
            flavor_rb = QRadioButton(fl)
            gb_v_box.addWidget(flavor_rb)
            self.wings_group.addButton(flavor_rb)

        wings_gbox.setLayout(gb_v_box)

        add_to_order_button2 = QPushButton("Add To Order")
        add_to_order_button2.clicked.connect(self.displayWingsInOrder)

        page2_v_box = QVBoxLayout()
        page2_v_box.addWidget(tab_wings_label)
        page2_v_box.addWidget(description_box)
        page2_v_box.addWidget(wings_gbox)
        page2_v_box.addWidget(add_to_order_button2, alignment=Qt.AlignRight)
        page2_v_box.addStretch()

        self.wings_tab.setLayout(page2_v_box)

    def collectTopingfInList(self):
        """
        Create list of all checked toppings radio  buttons.
        """
        return [button.text() for i, button in enumerate(self.toppings_group.buttons()) if button.isChecked()]

    def displayPizzaInOrder(self):
        """
        Collect the text from the radio buttons that are checked on pizza page.
        Display text in side widget.
        """
        try:
            pizza_text = self.crust_group.checkedButton().text()
            self.display_pizza_label.setText(pizza_text)

            toppings = self.collectTopingfInList()
            toppings_str = '\n'.join(toppings)
            self.display_toppings_label.setText(toppings_str)
            self.repaint()
        except AttributeError:
            print("No value selected.")
            QMessageBox.warning(self, "Error", "No value selected", QMessageBox.Ok)
            pass

    def displayWingsInOrder(self):
        """
        Collect the text from the radio buttons that are checked on wings page.
        Display text in side widget.
        """
        try:
            text = self.wings_group.checkedButton().text() + " Wings"
            self.display_wings_label.setText(text)
            self.repaint()
        except AttributeError:
            print("No value selected.")
        QMessageBox.warning(self, "Error", "No value selected", QMessageBox.Ok)
        pass


def loadImage(self, path):
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