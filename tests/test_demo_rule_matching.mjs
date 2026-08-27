import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import test from 'node:test';
import vm from 'node:vm';


const html = readFileSync(new URL('../demo/index.html', import.meta.url), 'utf8');
const start = html.indexOf('    const domainRules = [');
const end = html.indexOf('    function renderList', start);

assert.notEqual(start, -1, 'domain rule source is present');
assert.notEqual(end, -1, 'pure rule-matching source boundary is present');

const context = {};
vm.runInNewContext(
  `${html.slice(start, end)}
   globalThis.testDomainRules = domainRules;
   globalThis.testMatchesKeyword = matchesKeyword;`,
  context
);

function matchesRule(ruleName, text, useUnicode = true) {
  const rule = context.testDomainRules.find(({ name }) => name === ruleName);
  return rule.words.some((word) => context.testMatchesKeyword(text, word, useUnicode));
}

test('common inflections retain their intended domain', () => {
  for (const text of ['it failed', 'requests are failing', 'the UI is freezing']) {
    const expectedRule = text.includes('freezing') ? 'performance' : 'reliability';
    assert.equal(matchesRule(expectedRule, text), true, text);
  }
  assert.equal(matchesRule('performance', 'there is a slowdown'), true);
});

test('leading token boundaries still prevent substring false positives', () => {
  assert.equal(matchesRule('performance', 'the flag changed'), false);
  assert.equal(matchesRule('reliability', 'the profile is visible'), false);
});

test('ASCII fallback remains usable without Unicode property escapes', () => {
  assert.equal(context.testMatchesKeyword('the request failed', 'failed', false), true);
  assert.equal(context.testMatchesKeyword('the flag changed', 'lag', false), false);
});
