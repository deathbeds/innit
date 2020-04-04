# It's easy to configure a python package, `innit`?

    import innit

`innit` is a minimal configuration for building and documentating python projects using that shares metadata through the PEP 517 & 518 `"pyproject.toml"` configuration file.

The project is based on `flit` which configures metadata in `"pyproject"`.
`flit` provides a CLI to configure a basic module build. The metadata shares content that needed by `nikola and sphinx` for their configuration. Futhermore, the necessary metadata for a `flit` project would already be provided in a public Github repo.

`innit` configures projects using either a reference to a github repo or with CLI prompts. As much as possible, you should be using Github user interfaces to interact configure projects.

This configuration is ready to be used with Github Actions, Github Pages, and Read the Docs.

## files

* __pyproject.toml__ is configured for the [`flit` configuration][flit configuration].

* __conf.py__ can configure both `nikola and sphinx`. `nikola and sphinx` use the `str.upper and str.lower` namespaces meaning their are no name collisions, and they may be configured simulataneously.

* __setup.py__ runs `setuptools` using the __pyproject.toml__ configuration so that a module can be used in developer module with 

    ```bash
    pip install -e .
    ```

* __index.rst__ provides the table of contents for `sphinx`.

* __LICENSE__ can be created on github.

* __postBuild__ for binder.
## References

* [PEP517]
* [PEP518]
* https://snarky.ca/what-the-heck-is-pyproject-toml/

[flit configuration]: https://flit.readthedocs.io/en/latest/pyproject_toml.html
[binder]: #