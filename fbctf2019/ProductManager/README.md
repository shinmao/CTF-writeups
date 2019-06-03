# Product Manager
I spend a lot of time on finding vulnerability of sql injection on this challenge, but end up with finding that all the prepare statement are fucking perfect! After CTF has ended, I found a slide of Orange in 2015 about **column truncation vulnerability**!  
The vulnerability is based on `sql_mode`. Let's see the content of the variable on the online terminal:  
```
ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
```
If the mode includes `STRICT_ALL_TABLES`, the length of inserted data would be checked and blocked if it is too long! (Data too long for column...) However, if the mode is non-strict, the length would not be checked. Furthermore, based on the feature of mysql, mysql would automatically ignore the space character after the string, which means `admin         ` equals to `admin`!  
Next, let's see how **view product** works? In `view.php`, it would use `check_name_secret()` to find the matched pair of name and secret from DB, and return true if the result is not null. After checking, it would use `get_product` to return information of product. What's interesting, it uses `fetch_assoc()`, which would only return the first one of the matched result.  
Now, the way of payload is clear: First, add one more `facebook` to DB based on the column truncation vulnerability. Second, `fetch_assoc()` would still give us the information of the facebook which has been in DB.  
Find my payload in `exp.py`, and find flag in the following response:  
``
<p>Product details:<ul><li>facebook</li><li>Facebook, Inc. is an American online social media and social networking service company based in Menlo Park, California. Very cool! Here is a flag for you: fb{4774ck1n9_5q1_w17h0u7_1nj3c710n_15_4m421n9_:)}</li></ul></p><form action="/view.php" method="POST">
```
