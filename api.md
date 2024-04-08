# ReferenceSets

Methods:

- <code title="get /api/v1/referencesets/{id}">client.reference_sets.<a href="./src/sam/resources/reference_sets.py">retrieve</a>(id) -> BinaryAPIResponse</code>
- <code title="put /api/v1/referencesets/{id}">client.reference_sets.<a href="./src/sam/resources/reference_sets.py">update</a>(\*, path_id, \*\*<a href="src/sam/types/reference_set_update_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="delete /api/v1/referencesets/{id}">client.reference_sets.<a href="./src/sam/resources/reference_sets.py">delete</a>(id) -> None</code>

# ReferenceSessions

Methods:

- <code title="get /api/v1/referencesessions/{id}">client.reference_sessions.<a href="./src/sam/resources/reference_sessions.py">retrieve</a>(id) -> BinaryAPIResponse</code>
- <code title="put /api/v1/referencesessions/{id}">client.reference_sessions.<a href="./src/sam/resources/reference_sessions.py">update</a>(\*, path_id, \*\*<a href="src/sam/types/reference_session_update_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="delete /api/v1/referencesessions/{id}">client.reference_sessions.<a href="./src/sam/resources/reference_sessions.py">delete</a>(id) -> None</code>

# Organizations

Methods:

- <code title="put /api/v1/organizations">client.organizations.<a href="./src/sam/resources/organizations.py">update</a>(\*\*<a href="src/sam/types/organization_update_params.py">params</a>) -> BinaryAPIResponse</code>

# Members

Methods:

- <code title="put /api/v1/members/{memberId}">client.members.<a href="./src/sam/resources/members.py">update</a>(member_id, \*\*<a href="src/sam/types/member_update_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="delete /api/v1/members/{memberId}">client.members.<a href="./src/sam/resources/members.py">delete</a>(member_id) -> None</code>

# Feedbacks

Methods:

- <code title="put /api/v1/feedbacks/{feedback_id}">client.feedbacks.<a href="./src/sam/resources/feedbacks.py">update</a>(feedback_id, \*\*<a href="src/sam/types/feedback_update_params.py">params</a>) -> BinaryAPIResponse</code>

# Documents

Methods:

- <code title="get /api/v1/document/{doc_id}">client.documents.<a href="./src/sam/resources/documents.py">retrieve</a>(doc_id, \*\*<a href="src/sam/types/document_retrieve_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="put /api/v1/document/{doc_id}">client.documents.<a href="./src/sam/resources/documents.py">update</a>(doc_id, \*\*<a href="src/sam/types/document_update_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="delete /api/v1/document/{doc_id}">client.documents.<a href="./src/sam/resources/documents.py">delete</a>(doc_id) -> None</code>

# Corpora

Methods:

- <code title="get /api/v1/corpora/{corpus_id}">client.corpora.<a href="./src/sam/resources/corpora.py">retrieve</a>(corpus_id) -> BinaryAPIResponse</code>
- <code title="put /api/v1/corpora/{corpus_id}">client.corpora.<a href="./src/sam/resources/corpora.py">update</a>(corpus_id, \*\*<a href="src/sam/types/corpora_update_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="delete /api/v1/corpora/{corpus_id}">client.corpora.<a href="./src/sam/resources/corpora.py">delete</a>(corpus_id) -> None</code>

# Agents

Methods:

- <code title="get /api/v1/agents/{id}">client.agents.<a href="./src/sam/resources/agents/agents.py">retrieve</a>(id) -> BinaryAPIResponse</code>
- <code title="put /api/v1/agents/{id}">client.agents.<a href="./src/sam/resources/agents/agents.py">update</a>(id, \*\*<a href="src/sam/types/agent_update_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="delete /api/v1/agents/{id}">client.agents.<a href="./src/sam/resources/agents/agents.py">delete</a>(id) -> None</code>

## HiddenTags

Methods:

- <code title="put /api/v1/agents/{id}/hiddenTags">client.agents.hidden_tags.<a href="./src/sam/resources/agents/hidden_tags.py">update</a>(id, \*\*<a href="src/sam/types/agents/hidden_tag_update_params.py">params</a>) -> BinaryAPIResponse</code>

## Configs

Methods:

- <code title="get /api/v1/agents/{agentId}/configs/{integration}">client.agents.configs.<a href="./src/sam/resources/agents/configs/configs.py">retrieve</a>(integration, \*, agent_id) -> BinaryAPIResponse</code>
- <code title="put /api/v1/agents/{agentId}/configs/{integration}">client.agents.configs.<a href="./src/sam/resources/agents/configs/configs.py">update</a>(integration, \*, agent_id, \*\*<a href="src/sam/types/agents/config_update_params.py">params</a>) -> BinaryAPIResponse</code>

### Chat

Methods:

- <code title="get /api/v1/agents/{agentId}/configs/chat">client.agents.configs.chat.<a href="./src/sam/resources/agents/configs/chat.py">retrieve</a>(agent_id) -> BinaryAPIResponse</code>
- <code title="put /api/v1/agents/{agentId}/configs/chat">client.agents.configs.chat.<a href="./src/sam/resources/agents/configs/chat.py">update</a>(agent_id, \*\*<a href="src/sam/types/agents/configs/chat_update_params.py">params</a>) -> BinaryAPIResponse</code>

# ActionSets

Methods:

- <code title="get /api/v1/actionsets/{id}">client.action_sets.<a href="./src/sam/resources/action_sets.py">retrieve</a>(id) -> BinaryAPIResponse</code>
- <code title="put /api/v1/actionsets/{id}">client.action_sets.<a href="./src/sam/resources/action_sets.py">update</a>(\*, path_id, \*\*<a href="src/sam/types/action_set_update_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="delete /api/v1/actionsets/{id}">client.action_sets.<a href="./src/sam/resources/action_sets.py">delete</a>(id) -> None</code>

# Actions

Methods:

- <code title="get /api/v1/actions/{actionId}">client.actions.<a href="./src/sam/resources/actions.py">retrieve</a>(action_id) -> BinaryAPIResponse</code>
- <code title="put /api/v1/actions/{actionId}">client.actions.<a href="./src/sam/resources/actions.py">update</a>(action_id, \*\*<a href="src/sam/types/action_update_params.py">params</a>) -> BinaryAPIResponse</code>
