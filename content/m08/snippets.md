# Five snippets to review

**S1**
```js
function d(x) { return x * 1.2; }
```

**S2**
```js
const user = users.find((u) => u.id === id);
console.log(user.name);
```

**S3**
```js
const a = items.filter((i) => i.active).map((i) => i.price).reduce((s, p) => s + p, 0);
const b = orders.filter((o) => o.active).map((o) => o.price).reduce((s, p) => s + p, 0);
```

**S4**
```js
setTimeout(saveDraft, 86400000);
```

**S5**
```js
function formatPrice(cents) {
  return `$${(cents / 100).toFixed(2)}`;
}
// has two tests: 0 and 1999
```
