#include "widget.h"


Widget::Widget(QWidget *parent)
    : QWidget(parent)
{
    QFont buttonFont("Times", 20, QFont::Bold);
    button->setMinimumSize(200,100);
    button->setFont(buttonFont);

    connect(button,&QPushButton::clicked,[=](){
        qDebug() << "Button pressed";
    });

    button2->setMinimumSize(200,100);
    button2->setFont(buttonFont);
    button2->move(205,0);

    connect(button2,&QPushButton::pressed,[=](){
            qDebug() << "Button 2 pressed";
    });

    connect(button2,&QPushButton::released,[=](){
        qDebug() << "Button 2 released";
    });
}

Widget::~Widget()
{
}

