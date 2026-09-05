import type { ConfirmedIntent } from "../src/core/types";

declare const fields: Omit<ConfirmedIntent, "confirmedByHuman">;
const confirmed: ConfirmedIntent = { ...fields, confirmedByHuman: true };
// @ts-expect-error An unconfirmed hypothesis is not a ConfirmedIntent.
const unconfirmed: ConfirmedIntent = { ...fields, confirmedByHuman: false };
// @ts-expect-error Numeric truthiness is not human confirmation.
const numeric: ConfirmedIntent = { ...fields, confirmedByHuman: 1 };
// @ts-expect-error A textual claim is not a boolean confirmation.
const textual: ConfirmedIntent = { ...fields, confirmedByHuman: "true" };
// @ts-expect-error The admission flag is required.
const absent: ConfirmedIntent = fields;
void [confirmed, unconfirmed, numeric, textual, absent];
