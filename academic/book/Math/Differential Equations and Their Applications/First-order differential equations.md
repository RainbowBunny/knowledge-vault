---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-10-18T21:39
---
**Definition**: The general first-order linear differential equation is
$$\frac{dy}{dy} + a(t) y = b(t)$$
**Definition**: The equation
$$\frac{dy}{dt} + a(t) y = 0$$
is called the *homogeneous* first-order linear differential equation, and the equation above is called the *nonhomogeneous* first-order linear differential equation for $b(t)$ not identically zero.

*General solution:* $$y(t) = c \exp(-\int a(t) dt).$$
*Initial-value problem*: $$\frac{dy}{dt} + a(t) y = 0, \qquad y(t_0) = y_0$$
*Solution*:
$$y(t) = y(t_0) \exp (-\int_{t_0}^t a(s) ds) = y_0 \exp (-\int_{t_0}^t a(s) d s)$$
Idea to solve *nonhomogeneous* equation: 
$$\frac{dy}{dt}(\text{"Something"}) = b(t)$$
$$\mu(t) \frac{dy}{dt} + a(t) \mu(t) y = \mu(t) b(t)$$
$$\mu(t) = \exp(\int a(t) dt)$$
*Final solution*:
$$y = \frac{1}{\mu(t)}(\int \mu(t) b(t) dt + c) = \exp(-\int a(t) dt) (\int \mu (t) b(t) dt + c)$$
*IVP Solution:*
$$y = \frac{1}{\mu(t)} (\mu(t_0) y_0 + \int_{t_0}^t \mu(s) b(s) ds).$$

## The Van Meegeren art forgeries
## Population models

