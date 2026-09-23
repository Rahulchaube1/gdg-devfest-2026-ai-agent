# Agent Threat Model

## Assets
- user data
- credentials/secrets
- application state
- external API permissions
- model context
- evaluation integrity

## Trust boundaries
1. User → application
2. Application → model
3. Retrieval source → context
4. Model → tool gateway
5. Tool gateway → external system

## Primary risks
- prompt injection
- excessive agency
- unsafe tool arguments
- data leakage
- unauthorized state changes
- untraceable failures

## Controls
- input validation
- least privilege
- server-side authorization
- typed schemas
- approval gates
- data minimization
- audit logs
- behavioral evaluation
