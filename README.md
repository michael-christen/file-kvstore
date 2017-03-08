# repo_update
A way to monitor KPIs in a repo

## Architecture

This project aims to make it easy to setup KPI tracking in your repo.

It makes use of a configuration file for determining how metrics are gathered
and the order that they are stored in.

After installing the package, you get access to 2 helpful scripts:
* init_repo: configures your githook, and your initial configuration
* get_history: combines all past commits into a csv with the metrics

### Example configuration file

```yaml
---
- lines_of_code: "wc -l * | tail -n 1 | awk '{print $1}'"
```

