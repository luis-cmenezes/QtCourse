#include "rockwidget.h"
#include <QMessageBox>

RockWidget::RockWidget(QWidget *parent)  : QWidget{parent}
{
    setWindowTitle("Rock Widget Window");

    label->setText("Rock Widget Label");

    QPalette label2Palette;
    label2Palette.setColor(QPalette::Window,Qt::yellow);
    label2Palette.setColor(QPalette::WindowText,Qt::blue);

    QFont label2Font("Times",18,QFont::Bold);

    label2->setAutoFillBackground(true);
    label2->setFont(label2Font);
    label2->setText("Colored Label");
    label2->setPalette(label2Palette);
    label2->move(50,50);


    QFont buttonFont("Times",18,QFont::Bold);
    button->setText("Click me.");
    button->setFont(buttonFont);
    button->move(100,250);

    connect(button,SIGNAL(clicked()),this,SLOT(buttonClicked()));
}

void RockWidget::buttonClicked()
{
    QMessageBox::information(this,"Message","Button clicked");
}

QSize RockWidget::sizeHint() const
{
    return QSize(400,400);
}
