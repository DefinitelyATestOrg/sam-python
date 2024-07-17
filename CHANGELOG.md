# Changelog

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
