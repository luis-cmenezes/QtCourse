#ifndef ROCKWIDGET_H
#define ROCKWIDGET_H

#include <QWidget>
#include <QLabel>
#include <QPushButton>

class RockWidget : public QWidget
{
    Q_OBJECT
public:
    explicit RockWidget(QWidget *parent = nullptr);

    QLabel * label = new QLabel(this);
    QLabel * label2 = new QLabel(this);

    QPushButton * button = new QPushButton(this);

private slots:
    void buttonClicked();

private:
    QSize sizeHint() const;

signals:

};

#endif // ROCKWIDGET_H
