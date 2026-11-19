# Make the search faster with a delay and a cache

## What

The search now waits 300 milliseconds after the last key press before it calls the server. The app also keeps the last results in a cache.

## Why

Before this change the app called the server on every key press, so the search was slow and the server had too much work.

## How to test

1. Type a long word in the search box and check that the app sends only one request.
2. Search for the same word again and check that the results appear at once.

## Notes

The cache keeps only the last 20 searches, so the memory use stays small.
