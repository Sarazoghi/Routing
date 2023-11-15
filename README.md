# Routing
It Is A Project For Our AI Class;



The description of the problem is as follows: 

Ali recently started working in a restaurant as a courier.
His task is to pick up some food from the restaurant (origin) and go to all the destinations he is told once to deliver the food to the customer.
Unfortunately, the municipality has closed some of the city's streets, and Ali cannot cross the barriers.
Yab Restaurant, where Ali works, has signed a contract with some of the cafes in the city to give the couriers of this restaurant free of charge. As a result, Ali can go to these stores during his journey and consume the free item of that cafe to get energy.

علی به تازگی در یک رستوران به عنوان پیک موتوری شروع به کار کرده است.
وظیفه او این است که از رستوران (مبدا) تعدادی غذا را بگیرد و یک بار به تمام مقصد هایی که به او گفته می شود برود تا غذای مشتریان را تحویل دهد.
متاسفانه بعضی از خیابان های شهر توسط شهرداری بسته شده اند و علی نمی تواند از موانع گذاشته شده عبور کند.
رستورانی که علی در آن کار می کند با بعضی از کافه های شهر قرارداد بسته تا به پیک های موتوری این رستوران به صورت رایگان سرویس بدهند. در نتیجه علی میتواند در طول مسیر حرکت خود به این بستنی فروشی ها رفته و آیتم رایگان آن کافه را مصرف کند تا انرژی بگیرد.


The goal of the problem: find a transmission so that Ali can start moving with the most energy possible and visit all the customers at once. (Numerical energy is between negative infinity and positive infinity).


هدف مساله : مسیری را پیدا کنید تا علی با استفاده از آن بتواند با بیشترین انرژی ممکن از رستوران شروع به حرکت کرده و یک بار همه مشتریان را visit کند . (انرژی عددی بین منفی بی‌نهایت و مثبت بی‌نهایت است).

Limitations of the problem:
Ali can do only four actions:
Move up by one unit: U
Moving down by one unit: D
Move left by one unit: L
Move right by one unit: R

 محدودیت های مسئله :
علی میتواند فقط چهار عمل انجام دهد:
حرکت به بالا به اندازه یک واحد : U
حرکت به پایین به اندازه یک واحد : D
حرکت به چپ به اندازه یک واحد: L 
حرکت به راست به اندازه یک واحد: R

Ali cannot go out of the given range.
Ali can see all the streets and the energy that the use of that street takes from him.
​
علی نمیتواند از محدوده داده شده خارج شود.
علی میتواند تمام خیابان ها و انرژی ای که استفاده از آن خیابان ازش میگیرد را ببیند.

# PHASE ONE 
Implementation of the successor function

# PHASE TWO
1. BFS (Breadth First Search)
2. DFS (Depth First Search)
3. IDS (Iterative Deepening Search)
4. UCS (Uniform Cost Search)

# PHASE THREE
the Heuristic function should be implemented first, and then the following algorithms should be implemented:
5. A^*
6. Best First Search
