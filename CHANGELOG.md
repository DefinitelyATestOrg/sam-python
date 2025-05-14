# Changelog

## 0.15.0-alpha.12 (2025-05-14)

Full Changelog: [v0.15.0-alpha.11...v0.15.0-alpha.12](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.15.0-alpha.11...v0.15.0-alpha.12)

### Features

* **api:** my cool feature ([#250](https://github.com/DefinitelyATestOrg/sam-python/issues/250)) ([a47b826](https://github.com/DefinitelyATestOrg/sam-python/commit/a47b826f84d036b51e1ee6295637dd2ae730c795))
* cool cool cool ([#251](https://github.com/DefinitelyATestOrg/sam-python/issues/251)) ([253ec50](https://github.com/DefinitelyATestOrg/sam-python/commit/253ec50277ec1a42766c0cb5a43fc08d8b464528))


### Bug Fixes

* **package:** support direct resource imports ([6611818](https://github.com/DefinitelyATestOrg/sam-python/commit/6611818f6976350bd8e313910b5ef45b725a94aa))
* **perf:** optimize some hot paths ([b934ece](https://github.com/DefinitelyATestOrg/sam-python/commit/b934ece500851976dd6e3bee437ec5af5ca5cee1))
* **perf:** skip traversing types for NotGiven values ([63bd3fe](https://github.com/DefinitelyATestOrg/sam-python/commit/63bd3fec7eed946d9d5def7601a66de515f8ecf2))
* **pydantic v1:** more robust ModelField.annotation check ([2d01d23](https://github.com/DefinitelyATestOrg/sam-python/commit/2d01d23afe0ab3df17e7b99665edf105076bad80))


### Chores

* broadly detect json family of content-type headers ([a21bf3e](https://github.com/DefinitelyATestOrg/sam-python/commit/a21bf3ed1033a1d6055641bbaaf093d91cbd2b0f))
* **ci:** add timeout thresholds for CI jobs ([62a59a9](https://github.com/DefinitelyATestOrg/sam-python/commit/62a59a9d6c0b52c7d16d7fbfacd416c6b5968835))
* **ci:** only use depot for staging repos ([577d039](https://github.com/DefinitelyATestOrg/sam-python/commit/577d039ac4015b89bb2327f0f5c7911877b8137a))
* **ci:** run on more branches and use depot runners ([8af2b16](https://github.com/DefinitelyATestOrg/sam-python/commit/8af2b16a0b427f84966466e1bc942787e86c0cd4))
* **ci:** upload sdks to package manager ([eb1e41a](https://github.com/DefinitelyATestOrg/sam-python/commit/eb1e41ac840ebac39a77b7ad7c47d79990f6c634))
* **client:** minor internal fixes ([36002a4](https://github.com/DefinitelyATestOrg/sam-python/commit/36002a4352ab3fdfad756a0a1da23e875406725f))
* fix typos ([#244](https://github.com/DefinitelyATestOrg/sam-python/issues/244)) ([e17a94c](https://github.com/DefinitelyATestOrg/sam-python/commit/e17a94cc853d8d8edf35207ef9ac9afc7f09da37))
* **internal:** avoid errors for isinstance checks on proxies ([a1b2b16](https://github.com/DefinitelyATestOrg/sam-python/commit/a1b2b169a0ced82ff0c165ce2df2abf4317d1dd4))
* **internal:** base client updates ([49f7157](https://github.com/DefinitelyATestOrg/sam-python/commit/49f7157427c8707b7b2cdb24847aa46cc8385ed0))
* **internal:** bump pyright version ([2202d16](https://github.com/DefinitelyATestOrg/sam-python/commit/2202d16cdcb6fb483baa4e4362aafe3b6b583f9e))
* **internal:** codegen related update ([bb9bcf8](https://github.com/DefinitelyATestOrg/sam-python/commit/bb9bcf8ee8928653038d97a6f157e6f349f76fdf))
* **internal:** expand CI branch coverage ([#249](https://github.com/DefinitelyATestOrg/sam-python/issues/249)) ([4ad81be](https://github.com/DefinitelyATestOrg/sam-python/commit/4ad81be4ea6b88ab8c86d9be78dc7e54a633d42d))
* **internal:** fix list file params ([48cbc18](https://github.com/DefinitelyATestOrg/sam-python/commit/48cbc18ee1aa2202c942458d2ebb046072c4d72e))
* **internal:** import reformatting ([62efac5](https://github.com/DefinitelyATestOrg/sam-python/commit/62efac52fc86e548622e0d44414bf43e5dc48614))
* **internal:** minor formatting changes ([13ed47c](https://github.com/DefinitelyATestOrg/sam-python/commit/13ed47c99baa28c432e19a99b9191daf9a0b511c))
* **internal:** reduce CI branch coverage ([a99f5d3](https://github.com/DefinitelyATestOrg/sam-python/commit/a99f5d30b3eaff462c9c2bcbae124b5ec6184c34))
* **internal:** refactor retries to not use recursion ([1854460](https://github.com/DefinitelyATestOrg/sam-python/commit/185446009fdaa9766b1945fb411cd87591eff69f))
* **internal:** remove trailing character ([#246](https://github.com/DefinitelyATestOrg/sam-python/issues/246)) ([391b29b](https://github.com/DefinitelyATestOrg/sam-python/commit/391b29b078a53d37a9c20c56f00e5333f2de4e11))
* **internal:** slight transform perf improvement ([#248](https://github.com/DefinitelyATestOrg/sam-python/issues/248)) ([6f4d71b](https://github.com/DefinitelyATestOrg/sam-python/commit/6f4d71b16acb1175c9ec1dcb9e775e41db40121e))
* **internal:** update models test ([4edf616](https://github.com/DefinitelyATestOrg/sam-python/commit/4edf616353a9151e0328f219e88659cabeeb9128))
* **internal:** update pyright settings ([e7ed44b](https://github.com/DefinitelyATestOrg/sam-python/commit/e7ed44b71635476481a314046db0a485a9f71094))
* **internal:** variable name and test updates ([#247](https://github.com/DefinitelyATestOrg/sam-python/issues/247)) ([f5ef65b](https://github.com/DefinitelyATestOrg/sam-python/commit/f5ef65bc1e2381bb39ec5e58b203da53199f8ba5))

## 0.15.0-alpha.11 (2025-03-17)

Full Changelog: [v0.15.0-alpha.10...v0.15.0-alpha.11](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.15.0-alpha.10...v0.15.0-alpha.11)

### Bug Fixes

* **ci:** remove publishing patch ([#241](https://github.com/DefinitelyATestOrg/sam-python/issues/241)) ([8bfe755](https://github.com/DefinitelyATestOrg/sam-python/commit/8bfe7556dfb69033bfccd6bd9135955aa8fd647e))

## 0.15.0-alpha.10 (2025-03-17)

Full Changelog: [v0.15.0-alpha.9...v0.15.0-alpha.10](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.15.0-alpha.9...v0.15.0-alpha.10)

### Bug Fixes

* **ci:** ensure pip is always available ([#238](https://github.com/DefinitelyATestOrg/sam-python/issues/238)) ([b9f97c1](https://github.com/DefinitelyATestOrg/sam-python/commit/b9f97c1dc71e5f01a2b3b0b71ccf827ce7c6b11a))

## 0.15.0-alpha.9 (2025-03-14)

Full Changelog: [v0.15.0-alpha.8...v0.15.0-alpha.9](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.15.0-alpha.8...v0.15.0-alpha.9)

### Bug Fixes

* **types:** handle more discriminated union shapes ([#236](https://github.com/DefinitelyATestOrg/sam-python/issues/236)) ([0621fdf](https://github.com/DefinitelyATestOrg/sam-python/commit/0621fdfa3c8370a3381790212ef86b418576e59d))


### Chores

* **internal:** bump rye to 0.44.0 ([#234](https://github.com/DefinitelyATestOrg/sam-python/issues/234)) ([6b6ba5b](https://github.com/DefinitelyATestOrg/sam-python/commit/6b6ba5bd1c985ae45276fa9c2879617ed5b9a7cc))
* **internal:** codegen related update ([#235](https://github.com/DefinitelyATestOrg/sam-python/issues/235)) ([58a2924](https://github.com/DefinitelyATestOrg/sam-python/commit/58a2924d3a0b52912cb1d7228698006fa8966cbe))
* **internal:** remove extra empty newlines ([#233](https://github.com/DefinitelyATestOrg/sam-python/issues/233)) ([7ffeb47](https://github.com/DefinitelyATestOrg/sam-python/commit/7ffeb47770c0763e09ae76411bab67a20276cd7a))

## 0.15.0-alpha.8 (2025-03-10)

Full Changelog: [v0.15.0-alpha.7...v0.15.0-alpha.8](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.15.0-alpha.7...v0.15.0-alpha.8)

### Features

* **api:** api update ([#229](https://github.com/DefinitelyATestOrg/sam-python/issues/229)) ([d6e7435](https://github.com/DefinitelyATestOrg/sam-python/commit/d6e7435c09dd1c81174afe362ff9a15cbd97d967))


### Chores

* **docs:** update client docstring ([#227](https://github.com/DefinitelyATestOrg/sam-python/issues/227)) ([566923c](https://github.com/DefinitelyATestOrg/sam-python/commit/566923c54c22e7c6257863acb3de8d1642b9d998))
* **internal:** remove unused http client options forwarding ([#228](https://github.com/DefinitelyATestOrg/sam-python/issues/228)) ([29059a7](https://github.com/DefinitelyATestOrg/sam-python/commit/29059a765d2143e62f0467c373b888e2f16e8dc4))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#225](https://github.com/DefinitelyATestOrg/sam-python/issues/225)) ([652f288](https://github.com/DefinitelyATestOrg/sam-python/commit/652f288fe1b46050eec694241c638b4e4ac102a7))

## 0.15.0-alpha.7 (2025-02-25)

Full Changelog: [v0.15.0-alpha.6...v0.15.0-alpha.7](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.15.0-alpha.6...v0.15.0-alpha.7)

### Features

* **client:** allow passing `NotGiven` for body ([#221](https://github.com/DefinitelyATestOrg/sam-python/issues/221)) ([a93b2ca](https://github.com/DefinitelyATestOrg/sam-python/commit/a93b2ca797f24a745867ba860774e10d01191e2f))


### Bug Fixes

* **client:** mark some request bodies as optional ([a93b2ca](https://github.com/DefinitelyATestOrg/sam-python/commit/a93b2ca797f24a745867ba860774e10d01191e2f))


### Chores

* **internal:** fix devcontainers setup ([#222](https://github.com/DefinitelyATestOrg/sam-python/issues/222)) ([c1f7d19](https://github.com/DefinitelyATestOrg/sam-python/commit/c1f7d1987f80baf9f09e6388ea29cb502a215186))
* **internal:** properly set __pydantic_private__ ([#223](https://github.com/DefinitelyATestOrg/sam-python/issues/223)) ([a131f16](https://github.com/DefinitelyATestOrg/sam-python/commit/a131f16f65df467d585012ad020fafb413c297c4))
* **internal:** update client tests ([#219](https://github.com/DefinitelyATestOrg/sam-python/issues/219)) ([4bd9ccd](https://github.com/DefinitelyATestOrg/sam-python/commit/4bd9ccd122400e4bc44e3062d8fc289c0392ff9c))

## 0.15.0-alpha.6 (2025-02-14)

Full Changelog: [v0.15.0-alpha.5...v0.15.0-alpha.6](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.15.0-alpha.5...v0.15.0-alpha.6)

### Bug Fixes

* asyncify on non-asyncio runtimes ([#216](https://github.com/DefinitelyATestOrg/sam-python/issues/216)) ([104fee4](https://github.com/DefinitelyATestOrg/sam-python/commit/104fee4d627688e07e7f9badd80ab1da3cf53960))

## 0.15.0-alpha.5 (2025-02-14)

Full Changelog: [v0.15.0-alpha.4...v0.15.0-alpha.5](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.15.0-alpha.4...v0.15.0-alpha.5)

### Features

* **api:** manual updates ([#214](https://github.com/DefinitelyATestOrg/sam-python/issues/214)) ([c8001c5](https://github.com/DefinitelyATestOrg/sam-python/commit/c8001c5460ffdf1a3b4025dab3c407ce25a0fc16))
* **client:** send `X-Stainless-Read-Timeout` header ([#209](https://github.com/DefinitelyATestOrg/sam-python/issues/209)) ([1c4efe1](https://github.com/DefinitelyATestOrg/sam-python/commit/1c4efe1547a9dc6d00c5b2286f44179912fdb7f4))


### Chores

* **internal:** fix type traversing dictionary params ([#211](https://github.com/DefinitelyATestOrg/sam-python/issues/211)) ([c49a30e](https://github.com/DefinitelyATestOrg/sam-python/commit/c49a30e11fe6ce9e439c4b9b023e981bba891d82))
* **internal:** minor type handling changes ([#212](https://github.com/DefinitelyATestOrg/sam-python/issues/212)) ([1229f4a](https://github.com/DefinitelyATestOrg/sam-python/commit/1229f4a07c2cfb2dee1ed5ca789eca73879451b6))
* **internal:** update client tests ([#213](https://github.com/DefinitelyATestOrg/sam-python/issues/213)) ([93c3d71](https://github.com/DefinitelyATestOrg/sam-python/commit/93c3d711d5cd4d318c89fde38952b685bcebfe94))

## 0.15.0-alpha.4 (2025-02-05)

Full Changelog: [v0.15.0-alpha.3...v0.15.0-alpha.4](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.15.0-alpha.3...v0.15.0-alpha.4)

### Bug Fixes

* improve names for conflicting params ([#207](https://github.com/DefinitelyATestOrg/sam-python/issues/207)) ([bc4672b](https://github.com/DefinitelyATestOrg/sam-python/commit/bc4672b3285bd9edd19b6cf5cbe0c769fc1148f2))


### Chores

* **internal:** bummp ruff dependency ([#206](https://github.com/DefinitelyATestOrg/sam-python/issues/206)) ([59d91fa](https://github.com/DefinitelyATestOrg/sam-python/commit/59d91fac838800e957c8f4bea2f0f13034c515b4))
* **internal:** change default timeout to an int ([#204](https://github.com/DefinitelyATestOrg/sam-python/issues/204)) ([c609b25](https://github.com/DefinitelyATestOrg/sam-python/commit/c609b254e43897bb29afd4a97a6d76c733e89b9e))

## 0.15.0-alpha.3 (2025-02-05)

Full Changelog: [v0.15.0-alpha.1...v0.15.0-alpha.3](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.15.0-alpha.1...v0.15.0-alpha.3)

### Features

* **api:** manual updates ([#150](https://github.com/DefinitelyATestOrg/sam-python/issues/150)) ([b87822b](https://github.com/DefinitelyATestOrg/sam-python/commit/b87822b8cb6c547992c3aa65513baae590623310))
* **api:** manual updates ([#151](https://github.com/DefinitelyATestOrg/sam-python/issues/151)) ([429db3a](https://github.com/DefinitelyATestOrg/sam-python/commit/429db3affb1f0577231145c0cb0f34f0749df78c))
* **api:** manual updates ([#152](https://github.com/DefinitelyATestOrg/sam-python/issues/152)) ([b664659](https://github.com/DefinitelyATestOrg/sam-python/commit/b664659e4a4e6dcf988c069a111433cf740ba96c))
* **api:** manual updates ([#153](https://github.com/DefinitelyATestOrg/sam-python/issues/153)) ([6cb8c16](https://github.com/DefinitelyATestOrg/sam-python/commit/6cb8c168410b51f50e8c1b470f8d8c4ef90e386d))
* **api:** manual updates ([#154](https://github.com/DefinitelyATestOrg/sam-python/issues/154)) ([b5a1d7d](https://github.com/DefinitelyATestOrg/sam-python/commit/b5a1d7dacb9e134b166dee728ed825d7a6e6f1e1))
* **api:** manual updates ([#155](https://github.com/DefinitelyATestOrg/sam-python/issues/155)) ([cf5d457](https://github.com/DefinitelyATestOrg/sam-python/commit/cf5d4570061fc0f75a60da8acde84019a44283e8))
* **api:** OpenAPI spec update via Stainless API ([#156](https://github.com/DefinitelyATestOrg/sam-python/issues/156)) ([40f47c3](https://github.com/DefinitelyATestOrg/sam-python/commit/40f47c3b623cf69d169a0a3a4895591b185f695a))
* **api:** OpenAPI spec update via Stainless API ([#157](https://github.com/DefinitelyATestOrg/sam-python/issues/157)) ([c194e94](https://github.com/DefinitelyATestOrg/sam-python/commit/c194e9435c9ec73864a26dcb6ef4e079d8912dee))
* **api:** update via SDK Studio ([90099b1](https://github.com/DefinitelyATestOrg/sam-python/commit/90099b1d09e21af045870565fdf119e5c84c4045))
* **client:** add `retry_count` to raw response class ([#135](https://github.com/DefinitelyATestOrg/sam-python/issues/135)) ([1a03948](https://github.com/DefinitelyATestOrg/sam-python/commit/1a03948350ac1aacb58f14982c308df5bdf48f91))
* Document ability to update livestream video quality ([#315](https://github.com/DefinitelyATestOrg/sam-python/issues/315)) ([#186](https://github.com/DefinitelyATestOrg/sam-python/issues/186)) ([b35fce6](https://github.com/DefinitelyATestOrg/sam-python/commit/b35fce6de8edd76ccd02dbf17dc755860fbff88f))
* setup prod repos ([#185](https://github.com/DefinitelyATestOrg/sam-python/issues/185)) ([4dd9978](https://github.com/DefinitelyATestOrg/sam-python/commit/4dd9978089d5a6c1cc795e4ac80c1ca60dded948))
* some changes ([f647a37](https://github.com/DefinitelyATestOrg/sam-python/commit/f647a37d1f2940893e3122ca304e6f6d2458ebe7))


### Bug Fixes

* **client:** correctly serialise array body params ([#139](https://github.com/DefinitelyATestOrg/sam-python/issues/139)) ([f4402cc](https://github.com/DefinitelyATestOrg/sam-python/commit/f4402cc0757bae15608a451342bb387c52b67875))
* **client:** only call .close() when needed ([#191](https://github.com/DefinitelyATestOrg/sam-python/issues/191)) ([933330d](https://github.com/DefinitelyATestOrg/sam-python/commit/933330dda7e4222032ab33e44901aa3dddbe5d26))
* **tests:** make test_get_platform less flaky ([#199](https://github.com/DefinitelyATestOrg/sam-python/issues/199)) ([e8ff041](https://github.com/DefinitelyATestOrg/sam-python/commit/e8ff041af255e44ece9d68fdc0489b2f2815547e))


### Chores

* add missing isclass check ([#189](https://github.com/DefinitelyATestOrg/sam-python/issues/189)) ([65231c2](https://github.com/DefinitelyATestOrg/sam-python/commit/65231c223eb92b742d936f69b79e60a403be1fce))
* **ci:** also run pydantic v1 tests ([#149](https://github.com/DefinitelyATestOrg/sam-python/issues/149)) ([6f3ed78](https://github.com/DefinitelyATestOrg/sam-python/commit/6f3ed78fd065ffb65dba03bceb5a59b97faae1fe))
* **ci:** bump prism mock server version ([#141](https://github.com/DefinitelyATestOrg/sam-python/issues/141)) ([a8f3edd](https://github.com/DefinitelyATestOrg/sam-python/commit/a8f3edde6cc3d5c3d6a10dfba042bf33a8b23875))
* **client:** fix parsing union responses when non-json is returned ([#148](https://github.com/DefinitelyATestOrg/sam-python/issues/148)) ([00c7dd9](https://github.com/DefinitelyATestOrg/sam-python/commit/00c7dd945e536d843276e77a663835f07566e671))
* **examples:** minor formatting changes ([#143](https://github.com/DefinitelyATestOrg/sam-python/issues/143)) ([e979069](https://github.com/DefinitelyATestOrg/sam-python/commit/e97906940548063dff256bc3036ae827c10e1658))
* **internal:** add type construction helper ([#131](https://github.com/DefinitelyATestOrg/sam-python/issues/131)) ([b73dbea](https://github.com/DefinitelyATestOrg/sam-python/commit/b73dbea19c0828e67b47cb36a2ddf381dee2e7cf))
* **internal:** avoid pytest-asyncio deprecation warning ([#200](https://github.com/DefinitelyATestOrg/sam-python/issues/200)) ([e18e132](https://github.com/DefinitelyATestOrg/sam-python/commit/e18e132d0e6277a6bb0cd19fae67e3b8eb6e89ae))
* **internal:** bump httpx dependency ([#190](https://github.com/DefinitelyATestOrg/sam-python/issues/190)) ([ec1efed](https://github.com/DefinitelyATestOrg/sam-python/commit/ec1efed7c37fea79bf650e5afc943bc9f8488be9))
* **internal:** bump pyright ([#134](https://github.com/DefinitelyATestOrg/sam-python/issues/134)) ([fad61f5](https://github.com/DefinitelyATestOrg/sam-python/commit/fad61f5fe6464d387bedb05fd5f7f1343fd136ac))
* **internal:** bump pyright dependency ([#196](https://github.com/DefinitelyATestOrg/sam-python/issues/196)) ([4920a15](https://github.com/DefinitelyATestOrg/sam-python/commit/4920a151b369c2c1fc74188162f8e5d1068f6ce9))
* **internal:** bump ruff version ([#137](https://github.com/DefinitelyATestOrg/sam-python/issues/137)) ([309929b](https://github.com/DefinitelyATestOrg/sam-python/commit/309929b0ed02df5c864bae1b27f33e72e52fe5cb))
* **internal:** codegen related update ([#188](https://github.com/DefinitelyATestOrg/sam-python/issues/188)) ([bcde7bf](https://github.com/DefinitelyATestOrg/sam-python/commit/bcde7bfa0675fd1f75f65b299e762ad5cdcb0ecf))
* **internal:** codegen related update ([#193](https://github.com/DefinitelyATestOrg/sam-python/issues/193)) ([8279858](https://github.com/DefinitelyATestOrg/sam-python/commit/827985813fb87e9b7a424df7053af617c7345498))
* **internal:** codegen related update ([#194](https://github.com/DefinitelyATestOrg/sam-python/issues/194)) ([12a7357](https://github.com/DefinitelyATestOrg/sam-python/commit/12a7357976d8ac54aa39f5a0a0434d46459ae08a))
* **internal:** codegen related update ([#197](https://github.com/DefinitelyATestOrg/sam-python/issues/197)) ([d15d3f1](https://github.com/DefinitelyATestOrg/sam-python/commit/d15d3f1a2f3b3468efbea82071cb8bf5755c5cfd))
* **internal:** ensure package is importable in lint cmd ([#142](https://github.com/DefinitelyATestOrg/sam-python/issues/142)) ([28071e7](https://github.com/DefinitelyATestOrg/sam-python/commit/28071e72cacf41cfdaf9a8b8fe82f7f854ccf4d2))
* **internal:** fix some typos ([#187](https://github.com/DefinitelyATestOrg/sam-python/issues/187)) ([86f3d65](https://github.com/DefinitelyATestOrg/sam-python/commit/86f3d657ad4920493309505dfba681f3c8a842c6))
* **internal:** minor formatting changes ([#202](https://github.com/DefinitelyATestOrg/sam-python/issues/202)) ([ea76986](https://github.com/DefinitelyATestOrg/sam-python/commit/ea76986953a20c21fc431904b95d089c39224619))
* **internal:** minor style changes ([#201](https://github.com/DefinitelyATestOrg/sam-python/issues/201)) ([7f9fcb2](https://github.com/DefinitelyATestOrg/sam-python/commit/7f9fcb2d8156835f7aa4469e6c874549d9482205))
* **internal:** remove deprecated ruff config ([#140](https://github.com/DefinitelyATestOrg/sam-python/issues/140)) ([f2dd950](https://github.com/DefinitelyATestOrg/sam-python/commit/f2dd950e0df1134f1c5a02e6b0dfc068351c9fd0))
* **internal:** test updates ([#136](https://github.com/DefinitelyATestOrg/sam-python/issues/136)) ([9b96d28](https://github.com/DefinitelyATestOrg/sam-python/commit/9b96d286ea989f5ae004d62b19e6e9831a593bbb))
* **internal:** update deps ([#195](https://github.com/DefinitelyATestOrg/sam-python/issues/195)) ([b01c09e](https://github.com/DefinitelyATestOrg/sam-python/commit/b01c09e16e035463b0ae1cee41280d9d9e00fb2f))
* **internal:** update pydantic compat helper function ([#138](https://github.com/DefinitelyATestOrg/sam-python/issues/138)) ([18ad71a](https://github.com/DefinitelyATestOrg/sam-python/commit/18ad71a96b7f361e73c34c9c0b834021d6fca162))
* **internal:** use `TypeAlias` marker for type assignments ([#133](https://github.com/DefinitelyATestOrg/sam-python/issues/133)) ([9fc575b](https://github.com/DefinitelyATestOrg/sam-python/commit/9fc575b5c19836d185e5f49ecacdf609eb5202ca))
* **internal:** use different 32bit detection method ([#144](https://github.com/DefinitelyATestOrg/sam-python/issues/144)) ([f56d8c5](https://github.com/DefinitelyATestOrg/sam-python/commit/f56d8c59eeabee11d44a3fffcde47e51f5209d72))
* remove custom code ([c04ceee](https://github.com/DefinitelyATestOrg/sam-python/commit/c04ceee4c093989a532082fdf26d2c435e13931a))


### Documentation

* fix typos ([#192](https://github.com/DefinitelyATestOrg/sam-python/issues/192)) ([eaf2da0](https://github.com/DefinitelyATestOrg/sam-python/commit/eaf2da01c770c0407f2a7e731f0bb45cec8cffc4))
* **raw responses:** fix duplicate `the` ([#198](https://github.com/DefinitelyATestOrg/sam-python/issues/198)) ([27e98d2](https://github.com/DefinitelyATestOrg/sam-python/commit/27e98d291496bb8680382cd9097a93b308eeb5dc))

## 0.15.0-alpha.1 (2024-07-25)

Full Changelog: [v0.14.1-alpha.2...v0.15.0-alpha.1](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.14.1-alpha.2...v0.15.0-alpha.1)

### Features

* **api:** manual updates ([#126](https://github.com/DefinitelyATestOrg/sam-python/issues/126)) ([a7c2880](https://github.com/DefinitelyATestOrg/sam-python/commit/a7c2880df6b56cd41cb7e28ed295e36f368855c1))

## 0.14.1-alpha.2 (2024-07-25)

Full Changelog: [v0.14.1-alpha.1...v0.14.1-alpha.2](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.14.1-alpha.1...v0.14.1-alpha.2)

### Chores

* **internal:** version bump ([#124](https://github.com/DefinitelyATestOrg/sam-python/issues/124)) ([1ef2a28](https://github.com/DefinitelyATestOrg/sam-python/commit/1ef2a28c8478ef625551eabdea1d3c80e1ef758b))

## 0.14.1-alpha.1 (2024-07-25)

Full Changelog: [v0.14.0...v0.14.1-alpha.1](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.14.0...v0.14.1-alpha.1)

### Features

* **api:** manual updates ([#123](https://github.com/DefinitelyATestOrg/sam-python/issues/123)) ([2283208](https://github.com/DefinitelyATestOrg/sam-python/commit/22832081556d28213a4c2a66375814fe0b81ba75))


### Chores

* **ci:** limit release doctor target branches ([#118](https://github.com/DefinitelyATestOrg/sam-python/issues/118)) ([06c51ef](https://github.com/DefinitelyATestOrg/sam-python/commit/06c51ef797368e40430f7d8b21af57c13c6ac24b))
* **docs:** document how to do per-request http client customization ([#117](https://github.com/DefinitelyATestOrg/sam-python/issues/117)) ([1e030ba](https://github.com/DefinitelyATestOrg/sam-python/commit/1e030ba19b00f2f8cd783329d5b5a12fea18b8a8))
* **docs:** updating link ([#122](https://github.com/DefinitelyATestOrg/sam-python/issues/122)) ([3beba59](https://github.com/DefinitelyATestOrg/sam-python/commit/3beba591a5c0e3b9f78272503db36766314bb976))
* fix error message import example ([#121](https://github.com/DefinitelyATestOrg/sam-python/issues/121)) ([dcd0912](https://github.com/DefinitelyATestOrg/sam-python/commit/dcd09124139d46ae9a110077c4a0160e402dbebd))
* **tests:** update prism version ([#120](https://github.com/DefinitelyATestOrg/sam-python/issues/120)) ([016c994](https://github.com/DefinitelyATestOrg/sam-python/commit/016c9945b5a2726b6e91a770a969906143afe48a))
* update SDK settings ([#115](https://github.com/DefinitelyATestOrg/sam-python/issues/115)) ([f2c3573](https://github.com/DefinitelyATestOrg/sam-python/commit/f2c3573e2b027ea81190e2e0be875ecb20a7f013))


### Documentation

* **readme:** fix example snippet imports ([#119](https://github.com/DefinitelyATestOrg/sam-python/issues/119)) ([ea306ee](https://github.com/DefinitelyATestOrg/sam-python/commit/ea306eee19653ba56ffa68de9cf21a48f5b8266c))

## 0.14.0 (2024-07-17)

Full Changelog: [v0.13.0...v0.14.0](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.13.0...v0.14.0)

### Features

* **api:** manual updates ([#114](https://github.com/DefinitelyATestOrg/sam-python/issues/114)) ([0e8d1e1](https://github.com/DefinitelyATestOrg/sam-python/commit/0e8d1e1255b91434eb0ff17be0201406723556e0))


### Chores

* **ci:** also run workflows for PRs targeting `next` ([#106](https://github.com/DefinitelyATestOrg/sam-python/issues/106)) ([8d3d52a](https://github.com/DefinitelyATestOrg/sam-python/commit/8d3d52a4607c7a8adb09b0ea426ec4e7552846f0))
* **docs:** minor update to formatting of API link in README ([#112](https://github.com/DefinitelyATestOrg/sam-python/issues/112)) ([e13009f](https://github.com/DefinitelyATestOrg/sam-python/commit/e13009f91c8d302a99bba8fc623913257af29e6a))
* **internal:** add helper function ([#102](https://github.com/DefinitelyATestOrg/sam-python/issues/102)) ([09eb3d3](https://github.com/DefinitelyATestOrg/sam-python/commit/09eb3d3df8f35ccf2830f58aef52162e9efe7b72))
* **internal:** codegen related update ([#103](https://github.com/DefinitelyATestOrg/sam-python/issues/103)) ([b099a28](https://github.com/DefinitelyATestOrg/sam-python/commit/b099a281062b796dc324027f2614490dc59014a2))
* **internal:** codegen related update ([#105](https://github.com/DefinitelyATestOrg/sam-python/issues/105)) ([fbd4b52](https://github.com/DefinitelyATestOrg/sam-python/commit/fbd4b52ce7d6662226b36443f80abd7840d8ab1f))
* **internal:** codegen related update ([#109](https://github.com/DefinitelyATestOrg/sam-python/issues/109)) ([3cddcd4](https://github.com/DefinitelyATestOrg/sam-python/commit/3cddcd4461e47a426689088c3908bc4802367550))
* **internal:** codegen related update ([#111](https://github.com/DefinitelyATestOrg/sam-python/issues/111)) ([66feab9](https://github.com/DefinitelyATestOrg/sam-python/commit/66feab9e07bbc38e61fac8093a47c3956327366f))
* **internal:** codegen related update ([#99](https://github.com/DefinitelyATestOrg/sam-python/issues/99)) ([0464412](https://github.com/DefinitelyATestOrg/sam-python/commit/0464412f02feecdd0bb651bfc5593477b9774eec))
* **internal:** minor import restructuring ([#107](https://github.com/DefinitelyATestOrg/sam-python/issues/107)) ([15a4947](https://github.com/DefinitelyATestOrg/sam-python/commit/15a49478f27f4f39906efe24055103d57784312b))
* **internal:** minor options / compat functions updates ([#110](https://github.com/DefinitelyATestOrg/sam-python/issues/110)) ([b27e2c0](https://github.com/DefinitelyATestOrg/sam-python/commit/b27e2c0c175b2e3fb38e325670e9312a827b661c))
* **internal:** minor request options handling changes ([#101](https://github.com/DefinitelyATestOrg/sam-python/issues/101)) ([aa575ae](https://github.com/DefinitelyATestOrg/sam-python/commit/aa575aeadaab2b786377039f3909476025297fec))
* **internal:** update formatting ([#113](https://github.com/DefinitelyATestOrg/sam-python/issues/113)) ([b3de836](https://github.com/DefinitelyATestOrg/sam-python/commit/b3de836f35ca334891f182d2cefbba8d7ff9a466))
* **internal:** update mypy ([#104](https://github.com/DefinitelyATestOrg/sam-python/issues/104)) ([aee21ca](https://github.com/DefinitelyATestOrg/sam-python/commit/aee21ca70f0cb6e7effbd04ac4ba2ab92922b9bc))


### Documentation

* **examples:** use named params more ([#108](https://github.com/DefinitelyATestOrg/sam-python/issues/108)) ([f3931fb](https://github.com/DefinitelyATestOrg/sam-python/commit/f3931fb5967b71f3b02de6d6034a867ba9de6640))

## 0.13.0 (2024-07-17)

Full Changelog: [v0.12.5...v0.13.0](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.12.5...v0.13.0)

### Features

* **api:** manual updates ([#95](https://github.com/DefinitelyATestOrg/sam-python/issues/95)) ([8a1153f](https://github.com/DefinitelyATestOrg/sam-python/commit/8a1153f98c09b2e1578bff1aa6409448ab325dce))


### Chores

* **deps:** bump anyio to v4.4.0 ([#90](https://github.com/DefinitelyATestOrg/sam-python/issues/90)) ([533021c](https://github.com/DefinitelyATestOrg/sam-python/commit/533021cb723869b7ac8dc24791a2f27b0738521e))
* gitignore test server logs ([#93](https://github.com/DefinitelyATestOrg/sam-python/issues/93)) ([2e9cfbe](https://github.com/DefinitelyATestOrg/sam-python/commit/2e9cfbedf6004fffbaadb82497cd81cac51dd3a6))
* **internal:** add reflection helper function ([#92](https://github.com/DefinitelyATestOrg/sam-python/issues/92)) ([c8a563d](https://github.com/DefinitelyATestOrg/sam-python/commit/c8a563df367c1631547a3e52e7150a2dc89f7051))
* **internal:** add rich as a dev dependency ([#94](https://github.com/DefinitelyATestOrg/sam-python/issues/94)) ([6c24620](https://github.com/DefinitelyATestOrg/sam-python/commit/6c24620706cdb60a11f4a5918e0a9108cca07df2))

## 0.12.5 (2024-06-27)

Full Changelog: [v0.12.4...v0.12.5](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.12.4...v0.12.5)

### Bug Fixes

* **build:** include more files in sdist builds ([#87](https://github.com/DefinitelyATestOrg/sam-python/issues/87)) ([d9141be](https://github.com/DefinitelyATestOrg/sam-python/commit/d9141be425d1414d026695bbc2e240739ad5520d))

## 0.12.4 (2024-06-26)

Full Changelog: [v0.12.3...v0.12.4](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.12.3...v0.12.4)

### Bug Fixes

* temporarily patch upstream version to fix broken release flow ([#84](https://github.com/DefinitelyATestOrg/sam-python/issues/84)) ([61d9381](https://github.com/DefinitelyATestOrg/sam-python/commit/61d93814ae9b746cce274456bc547bb5bd7d942a))

## 0.12.3 (2024-06-25)

Full Changelog: [v0.12.2...v0.12.3](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.12.2...v0.12.3)

### Bug Fixes

* **docs:** fix link to advanced python httpx docs ([#81](https://github.com/DefinitelyATestOrg/sam-python/issues/81)) ([b71c291](https://github.com/DefinitelyATestOrg/sam-python/commit/b71c2910fb6955f22d0d2f4583d3b5cf083b2b0a))

## 0.12.2 (2024-06-19)

Full Changelog: [v0.12.1...v0.12.2](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.12.1...v0.12.2)

### Bug Fixes

* **client/async:** avoid blocking io call for platform headers ([#79](https://github.com/DefinitelyATestOrg/sam-python/issues/79)) ([6b763c4](https://github.com/DefinitelyATestOrg/sam-python/commit/6b763c45f492d285ec848a5f32daee4c1d903319))


### Chores

* **ci:** update rye install location ([#73](https://github.com/DefinitelyATestOrg/sam-python/issues/73)) ([15bffbe](https://github.com/DefinitelyATestOrg/sam-python/commit/15bffbe8ae5e4e5f24698f58504a5356fd94a9b3))
* **ci:** update rye install location ([#74](https://github.com/DefinitelyATestOrg/sam-python/issues/74)) ([6bf70ed](https://github.com/DefinitelyATestOrg/sam-python/commit/6bf70ed79d797d86cb52c1eafdf325295c10acbe))
* **client:** log response headers in debug mode ([#63](https://github.com/DefinitelyATestOrg/sam-python/issues/63)) ([2d7a79f](https://github.com/DefinitelyATestOrg/sam-python/commit/2d7a79f0922c74f44dc64f013cb3cb60f8b112c0))
* **docs:** add SECURITY.md ([#68](https://github.com/DefinitelyATestOrg/sam-python/issues/68)) ([3940313](https://github.com/DefinitelyATestOrg/sam-python/commit/3940313783968fedb771a98f29445a191ca2e58d))
* **internal:** add a `default_query` method ([#78](https://github.com/DefinitelyATestOrg/sam-python/issues/78)) ([893bba0](https://github.com/DefinitelyATestOrg/sam-python/commit/893bba06a77d48204d8478fe70c520382c8dc09d))
* **internal:** add scripts/test, scripts/mock and add ci job ([#64](https://github.com/DefinitelyATestOrg/sam-python/issues/64)) ([2fa9e46](https://github.com/DefinitelyATestOrg/sam-python/commit/2fa9e465084e461959e4b7ac1499d3be56376540))
* **internal:** add slightly better logging to scripts ([#71](https://github.com/DefinitelyATestOrg/sam-python/issues/71)) ([47d7e14](https://github.com/DefinitelyATestOrg/sam-python/commit/47d7e14633236f88c26522b011f5daafc4f2a52a))
* **internal:** bump mock server version to ~5.8.0 ([#65](https://github.com/DefinitelyATestOrg/sam-python/issues/65)) ([b3009fe](https://github.com/DefinitelyATestOrg/sam-python/commit/b3009fe545ffbdbfe277517359a11ffa30fa05ab))
* **internal:** bump pydantic dependency ([#69](https://github.com/DefinitelyATestOrg/sam-python/issues/69)) ([9feefd7](https://github.com/DefinitelyATestOrg/sam-python/commit/9feefd7f85fabbf694de4752b300ff93a154f69e))
* **internal:** bump pyright ([#75](https://github.com/DefinitelyATestOrg/sam-python/issues/75)) ([c15cf79](https://github.com/DefinitelyATestOrg/sam-python/commit/c15cf7955ee00c94cd43b7176dcb65d28d5b6884))
* **internal:** codegen related update ([#62](https://github.com/DefinitelyATestOrg/sam-python/issues/62)) ([c31fe8d](https://github.com/DefinitelyATestOrg/sam-python/commit/c31fe8df36402df3cffb745b9340bac533dba45d))
* **internal:** codegen related update ([#67](https://github.com/DefinitelyATestOrg/sam-python/issues/67)) ([847c78c](https://github.com/DefinitelyATestOrg/sam-python/commit/847c78cf52801282299f5c58ff4e9f29fda941c0))
* **internal:** codegen related update ([#70](https://github.com/DefinitelyATestOrg/sam-python/issues/70)) ([b83f859](https://github.com/DefinitelyATestOrg/sam-python/commit/b83f859c4e22aba1eb096e5ff07638e21e51db1f))
* **internal:** codegen related update ([#72](https://github.com/DefinitelyATestOrg/sam-python/issues/72)) ([7defe4d](https://github.com/DefinitelyATestOrg/sam-python/commit/7defe4d5d2f9d302fb8def837e794e9a78021638))
* **internal:** minor reformatting ([#61](https://github.com/DefinitelyATestOrg/sam-python/issues/61)) ([4256435](https://github.com/DefinitelyATestOrg/sam-python/commit/425643538c365bfceafefbda22593b68a3e03f44))
* **internal:** update bootstrap script ([#77](https://github.com/DefinitelyATestOrg/sam-python/issues/77)) ([8d51d6c](https://github.com/DefinitelyATestOrg/sam-python/commit/8d51d6c727b2bc8d7c5aeac8dae8b4be98ab0fca))
* **internal:** update test helper function ([#60](https://github.com/DefinitelyATestOrg/sam-python/issues/60)) ([7be0f6f](https://github.com/DefinitelyATestOrg/sam-python/commit/7be0f6fd201c3e77b868d4d05f85a988f02940d0))
* **internal:** use actions/checkout@v4 for codeflow ([#58](https://github.com/DefinitelyATestOrg/sam-python/issues/58)) ([61c1320](https://github.com/DefinitelyATestOrg/sam-python/commit/61c13205e2683cb864b67e53153f285ed0749654))


### Documentation

* **contributing:** update references to rye-up.com ([#76](https://github.com/DefinitelyATestOrg/sam-python/issues/76)) ([10a9ef2](https://github.com/DefinitelyATestOrg/sam-python/commit/10a9ef2f876434d86c9cba22ac58265ce836643c))
* **readme:** fix misleading timeout example value ([#66](https://github.com/DefinitelyATestOrg/sam-python/issues/66)) ([e3b37af](https://github.com/DefinitelyATestOrg/sam-python/commit/e3b37afe9f47bad5be6f3769a731d7b6ac683d59))

## 0.12.1 (2024-04-24)

Full Changelog: [v0.12.0...v0.12.1](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.12.0...v0.12.1)

### Bug Fixes

* **docs:** doc improvements ([#57](https://github.com/DefinitelyATestOrg/sam-python/issues/57)) ([100f363](https://github.com/DefinitelyATestOrg/sam-python/commit/100f36374ed11d8c847609c1fd26b38b93f0886e))


### Chores

* **internal:** add lru_cache helper function ([#48](https://github.com/DefinitelyATestOrg/sam-python/issues/48)) ([083ef52](https://github.com/DefinitelyATestOrg/sam-python/commit/083ef52474beb14ed7e1bcd28c7160940b748ec9))
* **internal:** ban usage of lru_cache ([#50](https://github.com/DefinitelyATestOrg/sam-python/issues/50)) ([fa629e5](https://github.com/DefinitelyATestOrg/sam-python/commit/fa629e5de56111a468a6d9d9e514af20d2b6e519))
* **internal:** bump pyright to 1.1.359 ([#55](https://github.com/DefinitelyATestOrg/sam-python/issues/55)) ([a11b72b](https://github.com/DefinitelyATestOrg/sam-python/commit/a11b72bbed119f84a2a4eb4e202bb780189f737e))
* rebuild project due to codegen change ([#51](https://github.com/DefinitelyATestOrg/sam-python/issues/51)) ([3840a85](https://github.com/DefinitelyATestOrg/sam-python/commit/3840a856c3acad0c4d3f8a2e5d019f052371bb0c))
* rename resource types ([#56](https://github.com/DefinitelyATestOrg/sam-python/issues/56)) ([db1e801](https://github.com/DefinitelyATestOrg/sam-python/commit/db1e801cbc2ad0b2fd6d9a35a0f1100bb20cb187))

## 0.12.0 (2024-04-15)

Full Changelog: [v0.11.0...v0.12.0](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.11.0...v0.12.0)

### Features

* **api:** update via SDK Studio ([#43](https://github.com/DefinitelyATestOrg/sam-python/issues/43)) ([946a504](https://github.com/DefinitelyATestOrg/sam-python/commit/946a5046ff6307b5e665cbc5ab845e77c2fb9bff))
* **api:** update via SDK Studio ([#45](https://github.com/DefinitelyATestOrg/sam-python/issues/45)) ([a17dc8d](https://github.com/DefinitelyATestOrg/sam-python/commit/a17dc8d1e83e0b8ce88e054277f1765586eab9b9))


### Chores

* go live ([#46](https://github.com/DefinitelyATestOrg/sam-python/issues/46)) ([1107b85](https://github.com/DefinitelyATestOrg/sam-python/commit/1107b8592a612a26b84d94d3cd2f8be685bdee2a))

## 0.11.0 (2024-04-05)

Full Changelog: [v0.10.0...v0.11.0](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.10.0...v0.11.0)

### Features

* **api:** update via SDK Studio ([#40](https://github.com/DefinitelyATestOrg/sam-python/issues/40)) ([0d69689](https://github.com/DefinitelyATestOrg/sam-python/commit/0d6968965ff8f5ada245de9d266022d2d9c65cb0))
* **api:** update via SDK Studio ([#42](https://github.com/DefinitelyATestOrg/sam-python/issues/42)) ([802561f](https://github.com/DefinitelyATestOrg/sam-python/commit/802561fd5c1beccb5a44193978f45491377af4db))

## 0.10.0 (2024-03-29)

Full Changelog: [v0.9.0...v0.10.0](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.9.0...v0.10.0)

### Features

* **api:** update via SDK Studio ([#38](https://github.com/DefinitelyATestOrg/sam-python/issues/38)) ([d6fa8ca](https://github.com/DefinitelyATestOrg/sam-python/commit/d6fa8ca9fe87ea3045b2486c3d6382c814501c3d))
* **api:** update via SDK Studio ([#39](https://github.com/DefinitelyATestOrg/sam-python/issues/39)) ([c04a420](https://github.com/DefinitelyATestOrg/sam-python/commit/c04a420651e8f06049b74a7b3d512df83e6e1a7f))
* OpenAPI spec update ([#26](https://github.com/DefinitelyATestOrg/sam-python/issues/26)) ([43ad6ec](https://github.com/DefinitelyATestOrg/sam-python/commit/43ad6ec1e6bfc4212321b9892076792183152038))
* OpenAPI spec update ([#28](https://github.com/DefinitelyATestOrg/sam-python/issues/28)) ([972e80f](https://github.com/DefinitelyATestOrg/sam-python/commit/972e80fa69e6c660c7657564c552535a19df3a44))
* OpenAPI spec update ([#29](https://github.com/DefinitelyATestOrg/sam-python/issues/29)) ([e6ac5ac](https://github.com/DefinitelyATestOrg/sam-python/commit/e6ac5ac180fb2f12e1e9a2ab58f0dfdd6a95b352))
* update via SDK Studio ([e1ed739](https://github.com/DefinitelyATestOrg/sam-python/commit/e1ed739248b1d70e194763104976f596c23a9cf5))
* update via SDK Studio ([#31](https://github.com/DefinitelyATestOrg/sam-python/issues/31)) ([c740d3c](https://github.com/DefinitelyATestOrg/sam-python/commit/c740d3c3afdda7ecdada0bcbcbf1f83265f10cff))
* update via SDK Studio ([#32](https://github.com/DefinitelyATestOrg/sam-python/issues/32)) ([40fa874](https://github.com/DefinitelyATestOrg/sam-python/commit/40fa8741bb35da635bc62425d3666a307ed8a4db))
* update via SDK Studio ([#34](https://github.com/DefinitelyATestOrg/sam-python/issues/34)) ([054e919](https://github.com/DefinitelyATestOrg/sam-python/commit/054e91958c2a2b1228a711a52027645d2cc97da2))
* update via SDK Studio ([#35](https://github.com/DefinitelyATestOrg/sam-python/issues/35)) ([b617109](https://github.com/DefinitelyATestOrg/sam-python/commit/b617109f9a814515d4329003924c7d8a46b8972d))
* update via SDK Studio ([#36](https://github.com/DefinitelyATestOrg/sam-python/issues/36)) ([b22aab0](https://github.com/DefinitelyATestOrg/sam-python/commit/b22aab0424418eb308f66d097bd1cd3b7c54684d))
* update via SDK Studio ([#37](https://github.com/DefinitelyATestOrg/sam-python/issues/37)) ([36f7b01](https://github.com/DefinitelyATestOrg/sam-python/commit/36f7b01d763fd00c6cb753906dc4ca876e76d51f))


### Chores

* configure new SDK language ([#33](https://github.com/DefinitelyATestOrg/sam-python/issues/33)) ([43b189b](https://github.com/DefinitelyATestOrg/sam-python/commit/43b189bbaaa51f9fe08daa36a22c0175ddb17353))

## 0.9.0 (2024-02-05)

Full Changelog: [v0.8.0...v0.9.0](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.8.0...v0.9.0)

### Features

* **api:** OpenAPI spec update ([#23](https://github.com/DefinitelyATestOrg/sam-python/issues/23)) ([01cd6c6](https://github.com/DefinitelyATestOrg/sam-python/commit/01cd6c696689a9f6f53b0ba629886f9b92329897))
* OpenAPI spec update ([#25](https://github.com/DefinitelyATestOrg/sam-python/issues/25)) ([fc31148](https://github.com/DefinitelyATestOrg/sam-python/commit/fc31148744212b563cde71bed967a7746dd1700c))

## 0.8.0 (2024-01-19)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.7.0...v0.8.0)

### Features

* **api:** OpenAPI spec update ([#21](https://github.com/DefinitelyATestOrg/sam-python/issues/21)) ([b027f11](https://github.com/DefinitelyATestOrg/sam-python/commit/b027f11bc6f0c2c5373012d65f8951cabbda455b))

## 0.7.0 (2024-01-12)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.6.0...v0.7.0)

### Features

* **api:** OpenAPI spec update ([#20](https://github.com/DefinitelyATestOrg/sam-python/issues/20)) ([6c2eddd](https://github.com/DefinitelyATestOrg/sam-python/commit/6c2eddd59b8868871d2c67ecee91dc90ab20fc63))


### Chores

* sam testing stuff ([#18](https://github.com/DefinitelyATestOrg/sam-python/issues/18)) ([ee65297](https://github.com/DefinitelyATestOrg/sam-python/commit/ee652973426d2fcc41dc4eb79067d00a32323452))

## 0.6.0 (2023-12-26)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.5.0...v0.6.0)

### Features

* **api:** OpenAPI spec update ([#16](https://github.com/DefinitelyATestOrg/sam-python/issues/16)) ([f89867d](https://github.com/DefinitelyATestOrg/sam-python/commit/f89867dce7a009304a7b0a7b612f5ec4b97ea3ef))

## 0.5.0 (2023-12-21)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.4.0...v0.5.0)

### Features

* **api:** OpenAPI spec update ([#14](https://github.com/DefinitelyATestOrg/sam-python/issues/14)) ([e7c6273](https://github.com/DefinitelyATestOrg/sam-python/commit/e7c627397a75cf7e02a2de052137f6ae56e3401d))

## 0.4.0 (2023-12-13)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.3.0...v0.4.0)

### Features

* **api:** OpenAPI spec update ([#12](https://github.com/DefinitelyATestOrg/sam-python/issues/12)) ([a391237](https://github.com/DefinitelyATestOrg/sam-python/commit/a391237b94fd409cdedf5d18c2c8aa66ed6c9237))

## 0.3.0 (2023-12-12)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.2.0...v0.3.0)

### Features

* **api:** OpenAPI spec update ([#9](https://github.com/DefinitelyATestOrg/sam-python/issues/9)) ([f9aa442](https://github.com/DefinitelyATestOrg/sam-python/commit/f9aa442c363ac321a7a1d71741d780207859bd0b))

## 0.2.0 (2023-12-12)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.1.0...v0.2.0)

### Features

* **api:** OpenAPI spec update ([#7](https://github.com/DefinitelyATestOrg/sam-python/issues/7)) ([382d5bd](https://github.com/DefinitelyATestOrg/sam-python/commit/382d5bd96f9d1c5cb9ea254fc6e0ed9f3b279baf))

## 0.1.0 (2023-12-08)

Full Changelog: [v0.0.2...v0.1.0](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.0.2...v0.1.0)

### Features

* **api:** OpenAPI spec update ([#5](https://github.com/DefinitelyATestOrg/sam-python/issues/5)) ([a51c58a](https://github.com/DefinitelyATestOrg/sam-python/commit/a51c58a353612bc4ede3d8415c270e5abb45bdde))

## 0.0.2 (2023-12-08)

Full Changelog: [v0.0.1...v0.0.2](https://github.com/DefinitelyATestOrg/sam-python/compare/v0.0.1...v0.0.2)

### Chores

* sam testing stuff ([4b57900](https://github.com/DefinitelyATestOrg/sam-python/commit/4b5790059ca9347479ebf62a6e2eab72e0230659))
* sam testing stuff ([#1](https://github.com/DefinitelyATestOrg/sam-python/issues/1)) ([1e16c0e](https://github.com/DefinitelyATestOrg/sam-python/commit/1e16c0e35ffb854af8687f8e04e97a4d238dc49a))
* sam testing stuff ([#2](https://github.com/DefinitelyATestOrg/sam-python/issues/2)) ([db07ce0](https://github.com/DefinitelyATestOrg/sam-python/commit/db07ce036aa66fea1c097eca4744087bdcb5e931))
* sam testing stuff ([#4](https://github.com/DefinitelyATestOrg/sam-python/issues/4)) ([b7d1c6a](https://github.com/DefinitelyATestOrg/sam-python/commit/b7d1c6a8bfee40f2d5b9f2199aaf7eb46edac664))
