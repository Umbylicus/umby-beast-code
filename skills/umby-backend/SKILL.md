---
name: umby-backend
description: Builds the server side of an app so it stays correct under retries, failures, and growth. Covers data modeling and migrations, API and server-action contracts, validation at the edges, error handling, background jobs, third-party integrations such as payments and messaging, and behavior tests. Use when building or changing a database schema, an API route, a webhook, a queue or scheduled job, an integration, a CRM or ordering backend, or any automation that writes data.
license: MIT
metadata:
  version: "1.0.0"
  tree: "umby-beast-code"
---

# Umby Backend

The interface can be redone in a day. Bad data lasts. Get the data and the contracts right first.

Read `../umby-architect/SKILL.md` for the stack choice and state modeling. Run `../umby-secure/SKILL.md` on anything that touches login, payments, or personal data.

## Step 1: Model the data

1. Write down the things the system tracks, how they relate, and which facts must always be true ("an order has at least one line", "a slot cannot be booked twice").
2. Put those facts in the database where you can: required columns, unique constraints, foreign keys, check constraints. A rule held only in application code will be broken by the next code path that forgets it.
3. Store each fact once. Compute the rest.
4. Money is whole minor units (cents) with a currency. Times are stored in UTC with the zone kept separately when it matters.
5. Give status fields a fixed set of values and write down which moves between them are allowed.

## Step 2: Change the schema safely

- Every schema change is a migration file in the repo. Never edit a production database by hand.
- Make changes that old and new code can both live with: add first, switch the code over, remove later.
- Test a migration against a copy of real-shaped data before it runs anywhere that matters.
- Dropping or rewriting data is irreversible. Stop and get an explicit go, and confirm a backup exists.

## Step 3: Define each contract before writing it

For every route, action, webhook, and job, write: who may call it, the input shape, the output shape, the errors it can return, and what it changes. Then:

- Validate input against a schema at the edge. Inside, trust the types.
- Check permission for the specific record, on the server, on every call.
- Return errors a caller can act on: a stable code, a human message, and no internal details.
- Page any list that can grow.

## Step 4: Make writes survive real conditions

- **Run it twice.** Requests get retried and buttons get double-clicked. A repeated call must leave the same result: use idempotency keys, unique constraints, or "create if missing".
- **Changes that belong together commit together.** Use a transaction. Do not hold one open across a call to another service.
- **Two users at once.** For anything with limited supply (stock, time slots, seats), let the database decide the winner with a constraint or a locked row. Do not check and then write as two separate steps.
- **Slow work leaves the request.** Sending email, calling slow services, and making files go to a background job with retries and a cap on attempts.

## Step 5: Integrations

- Wrap each outside service in one module, so the rest of the code never sees its raw response shapes.
- Set a timeout on every outside call. Decide ahead of time what the user sees when the service is down.
- Verify webhook signatures. Record the event id and skip repeats. Answer quickly and do the work in a job.
- Use the provider's test mode and test credentials while building. Live keys are entered by the operator, not by you.
- Never invent an API's behavior. Read its current documentation, and say when you could not.

## Step 6: See what it is doing

- Log each request's outcome with an id that follows it through jobs and outside calls. No secrets or personal data in logs.
- Errors go somewhere a person will see them.
- A health check tells whether the service and its database are reachable.

## Step 7: Test behavior

Test through the contract: call the route, look at the response and the stored data. Cover the main path, each validation failure, a caller with no permission, a repeated call, and the outside service failing. Use a real test database, not a mocked one, for anything that depends on constraints or transactions.

## Definition of done

Rules about the data are enforced by the database where possible. Every contract validates input and checks permission on the server. Each write was shown safe to repeat. Migrations are in the repo and tested. The behavior tests pass. Outside-service failures have a defined result.
