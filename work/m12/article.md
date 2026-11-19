# How I stopped a slow search with a small delay

When I built a search box for my app, it felt slow. Every time I typed a letter, the app called the server. This made the page slow and it used a lot of data. In this article I explain how a small delay fixed the problem.

## The problem

The search box sent a request on every key press. If a user typed the word "keyboard", the app made eight requests in less than two seconds. Most answers were not useful, because the user was still typing. The server had more work than needed, and the screen showed old results for a short time.

## The solution

The idea is simple. The app should wait until the user stops typing for a short time, and then it sends only one request. This idea has a name: debounce. First, I wrote a small function that waits 300 milliseconds. Then I used it in the search box. If the user types again before the time ends, the timer starts again.

```js
function debounce(action, delay) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => action(...args), delay);
  };
}
```

I also added a small cache. When the user searches the same word again, the app shows the saved result at once and does not call the server.

## What I learned

First, small changes can make a big difference for the user. The number of requests went down from eight to one for a normal word. Second, I learned that a good name for an idea helps me to search for answers. When I found the word debounce, I found many good examples. Finally, I learned to measure before and after a change. The numbers showed me that the change really helped.

## Conclusion

A delay of 300 milliseconds made the search faster, cheaper and easier to use. If you have a search box that feels slow, try a debounce function first. It takes only a few lines of code and it is easy to test. Next, I want to learn how to cancel old requests, so the screen never shows old results.
