# Final Project: Building a Simple Web Application

You have all the pieces. Classes and constructor promotion, namespaces and Composer, arrays and collections, exceptions, interfaces: the previous chapters handed you the working vocabulary of modern PHP, one word at a time. **This chapter assembles those pieces into one small, coherent thing: a web application built from nothing but PHP itself.**

No framework, on purpose. You will probably use Laravel or Symfony at work, and you should. But using one before you have built something without it means taking its conveniences on faith. Router, controller, view: these are only names for patterns that fall out naturally when you solve the small problems every web application faces. Build them once by hand, at this scale, and everything a framework does later reads as "that is the thing I already understand" instead of magic.

The build has three steps. First, the smallest router that could work: one file, PHP's own development server, and a few `if` statements deciding what to send back. Then that file grows into something shaped like MVC, with real controller classes and PHP's oldest talent, templating, put to proper use. Last, a look at how a request's life actually ends, and how to run cleanup code at that exact moment, which brings back the request model from [Chapter 18](ch18-01-request-model.md).

Well under two hundred lines in total. What you keep afterwards is bigger than the code: a clear picture of what happens underneath the frameworks you will reach for next.
