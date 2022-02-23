#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QPushButton>
#include <QPushButton>
#include <QDebug>

class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();


private:
    QPushButton *button = new QPushButton("Button1",this);
    QPushButton *button2 = new QPushButton("Button2",this);

};
#endif // WIDGET_H
