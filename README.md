# Annotation Agreement Kit

Computes observed agreement, expected agreement, Cohen’s kappa, and disagreement indexes for two aligned label sequences.

```bash
python -m unittest discover -s tests -v
python -m pip install .
annotation-agreement labels.json
```

```json
{"left":["cat","dog"],"right":["cat","cat"]}
```

This package supports two-rater, categorical agreement. It does not replace annotation-guideline review, adjudication, or multi-rater analysis.

## License

MIT.
