#include "widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
{
    firstNameLabel->setMinimumSize(70,30);
    firstNameLabel->move(10,10);

    firstNameLineEdit->setMinimumSize(200,30);
    firstNameLineEdit->move(100,10);

    lastNameLabel->setMinimumSize(70,30);
    lastNameLabel->move(10,50);

    lastNameLineEdit->setMinimumSize(200,30);
    lastNameLineEdit->move(100,50);

    cityLabel->setMinimumSize(70,30);
    cityLabel->move(10,90);

    cityLineEdit->setMinimumSize(200,30);
    cityLineEdit->move(100,90);

    QFont grabDataFont("Times", 20, QFont::Bold);
    grabDataButton->setFont(grabDataFont);
    grabDataButton->move(80,140);

    firstNameLineEdit->setPlaceholderText("Your first name");
    lastNameLineEdit->setPlaceholderText("Your last name");
    cityLineEdit->setPlaceholderText("Your current city");

    connect(grabDataButton,&QPushButton::clicked,[=]()
    {
        QString firstName = firstNameLineEdit->text();
        QString lastName = lastNameLineEdit->text();
        QString city = cityLineEdit->text();

        if(!firstName.isEmpty() && !lastName.isEmpty() && !city.isEmpty())
        {
            qDebug() << firstName;
            qDebug() << lastName;
            qDebug() << city;
        }else
        {
            QMessageBox::warning(this,"Input error","Not all inputs are fulfilled", QMessageBox::Ok);
        }

    });

    connect(firstNameLineEdit,&QLineEdit::returnPressed,[=]()
    {
        lastNameLineEdit->setFocus();
    });

    connect(lastNameLineEdit,&QLineEdit::returnPressed,[=]()
    {
        cityLineEdit->setFocus();
    });

    connect(cityLineEdit,&QLineEdit::returnPressed,[=]()
    {
        grabDataButton->clicked(true);
    });
}

Widget::~Widget()
{
}

