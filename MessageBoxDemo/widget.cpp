#include "widget.h"
#include <QPushButton>
#include <QMessageBox>
#include <QDebug>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
{
    QPushButton *button = new QPushButton(this);
    button->setText("Click here");
    button->move(200,200);
    connect(button,&QPushButton::clicked,[=](){

        /*
        QMessageBox message;
        message.setMaximumSize(300,200);
        message.setWindowTitle("Message Title");
        message.setText("Button clicked");
        message.setInformativeText("Do you want to do something about it ?");
        message.setIcon(QMessageBox::Critical);
        message.setStandardButtons(QMessageBox::Ok | QMessageBox::Cancel);
        message.setDefaultButton(QMessageBox::Cancel);

        int msgBoxReturn = message.exec();
        */

        /*
        int msgBoxReturn = QMessageBox::critical(this,"Message title","Button clicked. Do you want to do something ?",
                                                QMessageBox::Ok|QMessageBox::Cancel);
        */

        /*
        int msgBoxReturn = QMessageBox::information(this,"Message title","Button clicked. Do you want to do something ?",
                                                QMessageBox::Ok|QMessageBox::Cancel);
        */

        /*
        int msgBoxReturn = QMessageBox::question(this,"Message title","Button clicked. Do you want to do something ?",
                                                QMessageBox::Ok|QMessageBox::Cancel);
        */

        int msgBoxReturn = QMessageBox::warning(this,"Message title","Button clicked. Do you want to do something ?",
                                                QMessageBox::Ok|QMessageBox::Cancel);

        if(msgBoxReturn == QMessageBox::Ok)
        {
            qDebug() << "User clicked on OK.";
        }else
        {
            qDebug() << "User clicked on Cancel.";
        }
    });
}

Widget::~Widget()
{
}

