---
name: secure
description: Reviews a build for the security and privacy mistakes that actually hurt small products: exposed secrets, missing permission checks, unvalidated input, unsafe payment and webhook handling, leaky data, and risky dependencies. Works from the real attack paths of the thing being built and reports only findings it can demonstrate. Use before launch, whenever a change touches login, permissions, payments, file uploads, user data, webhooks, or API routes, and when asked for a security check.
license: MIT
metadata:
  version: "1.0.0"
  tree: "beast-code"
---

# Secure

A defensive review of your own build. Report what you can show, with the request or line that shows it. A list of theoretical worries helps nobody.

## Step 1: Map what can be attacked

Write a short list before reading code closely:

- every way in: pages, API routes, webhooks, file uploads, admin screens, scheduled jobs
- every kind of user, including "not signed in", and what each should be able to do
- the valuable things: accounts, payment actions, personal data, admin powers, API keys

## Step 2: Check each area

**Secrets**
- No keys, tokens, or passwords in the repo, in client-side code, or in logs. Search the code and the built output.
- Secret keys live in server-side environment variables. Only keys meant to be public reach the browser.
- A committed secret is burned. Tell the operator to rotate it. Deleting the line is not enough.

**Who can do what**
- Every server route checks that the caller is signed in **and** is allowed to touch that specific record. Test it: as user A, request user B's record by id.
- Permission checks run on the server. A hidden button is not a permission check.
- Admin routes check for admin on every request.

**Input**
- Everything from outside (forms, query strings, headers, uploads, webhooks, third-party APIs) is validated on the server against a schema before use.
- Database queries use parameters, never string-built SQL.
- User content shown in a page is escaped. Raw HTML insertion is used only on sanitized content.
- Uploads: limit type and size, store outside the code path, never run them.
- The server does not fetch arbitrary user-supplied URLs.

**Sessions and login**
- Use the platform's or a maintained library's auth. Do not write your own password or session code.
- Cookies are `HttpOnly`, `Secure`, and `SameSite`. State-changing requests are protected against cross-site forgery.
- Login, signup, and password reset are rate-limited, and their errors do not reveal whether an account exists.

**Payments and webhooks**
- Prices and totals are computed on the server from your own data. Never trust an amount sent by the browser.
- Webhooks verify the provider's signature before doing anything.
- Webhook handlers and payment actions are safe to run twice: use the provider's event id or an idempotency key.
- Card data goes straight to the payment provider's hosted fields. It never touches your server or logs.

**Data**
- Collect only what the product needs. Personal data is not in logs, URLs, or analytics events.
- API responses return only the fields the screen needs, not whole database rows.
- Backups exist, and someone has restored one.

**Dependencies and setup**
- Run the package manager's audit. Fix high-severity findings in code that ships.
- No debug modes, sample accounts, or open admin panels in production settings.
- Security headers and HTTPS are on. Error pages do not show stack traces.

## Step 3: Report

For each finding: where, what an attacker could do, how you showed it (the request, the line, the output), and the fix. Rank by harm. Mark anything you suspect but could not show as **unconfirmed**.

Fix findings only when the task asked for fixes. Auth, billing, and customer data are protected code under the standing rules, so ask before changing them.

## Definition of done

Every way in from Step 1 was checked against Step 2. Each finding has evidence or is marked unconfirmed. Committed secrets were flagged for rotation. The report says what was not checked.
