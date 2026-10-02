# Project Bounties Guide

This document provides the official template for proposing and claiming bounties within the MineAgent project. To ensure that bounties are machine-scannable and clear for all contributors, please follow the format below.

## Bounty Proposal Template

When creating a new bounty issue, please use the following markdown structure:

```markdown
[Bounty] $XXX – [Title of the Task]

## Problem in plain language
[Provide a concise and precise description of the problem or the feature requested]

## Technical Requirements / Formal Statement
[If applicable, provide the formal statement, API specifications, or Lean 4 code. Otherwise, specify that the bounty hunter must produce the formalization.]

```lean
-- Example for mathematical tasks
import Mathlib.Data.Nat.Prime
example (n : ℕ) (hn : n > 1) : ∃ p, Prime p ∧ [predicate] := sorry
```

## Bounty Goals
Choose one or both:
- **A) Implementation/Proof**: Complete the task and provide a working solution. 
  Bounty: $___
- **B) Disproof/Counterexample**: Provide a concrete counterexample or proof of impossibility.
  Bounty: $___

## Merge / Acceptance Criteria
For the bounty to be paid and the contribution merged:
- The work must be submitted as a Pull Request to this repository.
- The PR must include clear documentation and pass all CI tests.
- All code must follow the project's style guide.
- The PR must be merged by a maintainer.

## Metadata for Automation
- **Labels**: `bounty`, `help-wanted`
- **Required Phrase**: The PR description must contain the exact phrase "[Bounty Name] bounty"

## License
All contributed code will be released under the project's default license (MIT).

## How to Claim
1. Fork this repository.
2. Implement the solution.
3. Reference the bounty issue in the PR description.
4. Once merged, payment will be processed within 7 days.
```

## Tips for Bounty Hunters
- Ensure your PR is clean and follows the commit convention.
- Always link the issue you are solving.
- Use the `/claim` command if the project uses a claim bot.
