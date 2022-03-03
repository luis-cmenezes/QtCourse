#include "widget.h"
#include "ui_widget.h"
#include <stdlib.h>
#include <time.h>
#include <QDebug>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);
    ui->startOverButton->setDisabled(true);
    ui->messageLabel->setText("");

    srand(time(NULL));
    correctNumber = rand() % 10 + 1;

    qDebug() << "Secret number generated: " << QString::number(correctNumber);
}

Widget::~Widget()
{
    delete ui;
}


void Widget::on_guessButton_clicked()
{
    guessNumber = ui->spinBox->value();
    qDebug() << "The guess number is: " << QString::number(guessNumber);

    if(guessNumber == correctNumber)
    {
        ui->messageLabel->setText("Congratulations, number is: "+QString::number(guessNumber));
        ui->guessButton->setDisabled(true);
        ui->startOverButton->setDisabled(false);

    }else
    {
        if(guessNumber < correctNumber)
        {
            ui->messageLabel->setText("Number is higher than "+QString::number(guessNumber));
        }
        else
        {
            ui->messageLabel->setText("Number is lower than "+QString::number(guessNumber));
        }
    }
}

void Widget::on_startOverButton_clicked()
{
    ui->guessButton->setDisabled(false);
    ui->startOverButton->setDisabled(true);
    ui->spinBox->setValue(1);
    ui->messageLabel->setText("");

    correctNumber = rand() % 10 + 1;

    qDebug() << "Secret number generated: " << QString::number(correctNumber);
}

