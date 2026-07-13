"""
Stack Practice: Browser History
===============================

Goal:
Practice stack using Python list.

A stack follows this rule:

    Last In, First Out

That means:
- The last page you visit is the current page.
- When you go back, you remove the current page.
- Then the previous page becomes the current page.

You will practice:
- class
- __init__
- list
- append
- pop
- method
- edge cases


Task
----

Create a class called BrowserHistory.

It should support these methods:


1. visit(page)

Add a new page to the browser history.

Example:

    browser.visit("google.com")
    browser.visit("github.com")

The internal history should become:

    ["google.com", "github.com"]


2. back()

Go back to the previous page.

Rules:

- If there are at least 2 pages in history:
    remove the current page
    return the new current page

- If there is only 1 page or 0 pages:
    return "No page to go back"

Example:

    browser = BrowserHistory()

    browser.visit("google.com")
    browser.visit("github.com")
    browser.visit("stackoverflow.com")

    print(browser.back())
    # github.com

    print(browser.back())
    # google.com

    print(browser.back())
    # No page to go back


3. current_page()

Return the current page.

Rules:

- If history is not empty:
    return the last page in the history

- If history is empty:
    return "No page visited"


4. forward()

Go forward to the next page after using back().

This is similar to a real browser:

    visit google.com
    visit github.com
    visit stackoverflow.com

    back()
    # current page becomes github.com

    forward()
    # current page becomes stackoverflow.com again

Hint:
- You probably need another list to store pages that were removed by back().
- This second list can also work like a stack.

Rules:

- When back() removes the current page:
    save that removed page somewhere

- When forward() is called:
    if there is a page saved for going forward:
        move that page back into history
        return the current page

    otherwise:
        return "No page to go forward"

- When visit(page) is called after going back:
    clear the forward history

Example:

    browser = BrowserHistory()

    browser.visit("google.com")
    browser.visit("github.com")
    browser.visit("stackoverflow.com")

    print(browser.back())
    # github.com

    print(browser.forward())
    # stackoverflow.com

    print(browser.back())
    # github.com

    browser.visit("python.org")

    print(browser.forward())
    # No page to go forward


Expected behavior
-----------------

browser = BrowserHistory()

print(browser.current_page())
# No page visited

browser.visit("google.com")
browser.visit("github.com")
browser.visit("stackoverflow.com")

print(browser.current_page())
# stackoverflow.com

print(browser.back())
# github.com

print(browser.back())
# google.com

print(browser.back())
# No page to go back

print(browser.current_page())
# google.com


Suggested structure
-------------------

class BrowserHistory:
    def __init__(self):
        # TODO: Create an empty list to store history
        # TODO for the next step: Create another empty list for forward history
        pass

    def visit(self, page):
        # TODO: Add page to history
        # TODO for the next step: Clear forward history when visiting a new page
        pass

    def back(self):
        # TODO: Go back to previous page
        # TODO for the next step: Save the removed page so forward() can use it
        pass

    def forward(self):
        # TODO: Go forward to the next page
        pass

    def current_page(self):
        # TODO: Return current page
        pass


def main():
    browser = BrowserHistory()

    print(browser.current_page())

    browser.visit("google.com")
    browser.visit("github.com")
    browser.visit("stackoverflow.com")

    print(browser.current_page())

    print(browser.back())
    print(browser.back())
    print(browser.back())

    print(browser.current_page())


if __name__ == "__main__":
    main()
"""


class BrowserHistory:
    def __init__(self):
        # TODO: Create an empty list to store history
        self.history = []
        # TODO next: Create another list for forward history
        self.history_forward = []

    def visit(self, page):
        # TODO: Add page to history
        self.history.append(page)
        # TODO next: If the user visits a new page, clear forward history
        self.history_forward.clear()
        
    

    def back(self):
        # TODO: Go back to previous page
        # TODO next: When you pop the current page, save it for forward()
        if len(self.history) >= 2:
            self.history_forward.append(self.history.pop())
            return self.history[-1]
        else:
            return "No page to go back"
        
        


    def forward(self):
        # TODO next: Go forward to the next page if possible
        if len(self.history_forward) >= 1:
            last = self.history_forward.pop()
            self.history.append(last)
            return last
        else:
            return "No page to go forward"
        #def forward(self):
            #if len(self.history_forward) == 0:
                #return "No page to go forward"

            #last = self.history_forward.pop()
            #self.history.append(last)
            #return last

    def current_page(self):
        # TODO: Return current page
        if len(self.history) == 0:
            return "No page visited"

        return self.history[-1]
        


def main():
    browser = BrowserHistory()
    print(browser.current_page())

    browser.visit("google.com")
    browser.visit("github.com")
    browser.visit("stackoverflow.com")

    print(browser.current_page())

    print(browser.back())
    print(browser.back())
    print(browser.back())

    print(browser.current_page())


if __name__ == "__main__":
    main()
