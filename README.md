\# Projet DevOps - Atelier Git avancé



\## Équipe simulée



\- Ahmed1 : développement

\- Ahmed2 : documentation

\- Ahmed3 : revue et sécurité



\## Stratégie de branches



Nous utilisons une stratégie Trunk-Based Development.



La branche `main` contient la version stable du projet.



Les nouvelles modifications sont réalisées sur des branches courtes.



\### Convention de nommage



\- feat/... : nouvelle fonctionnalité

\- fix/... : correction

\- docs/... : documentation

\- hotfix/... : correction urgente



Exemples :



\- feat/greeting

\- fix/validation

\- docs/architecture



\## Règle de merge



Les modifications doivent être intégrées dans `main` via une Pull Request.



Nous utiliserons un historique linéaire avec Squash Merge ou Rebase Merge.



\## Convention de commits



Nous utilisons Conventional Commits :



\- feat: nouvelle fonctionnalité

\- fix: correction

\- docs: documentation

\- chore: maintenance

## Port validation

The application validates TCP/UDP port numbers.
Valid ports range from 1 to 65535.
Port validation is used by the networking module.
Validation tests are executed before release.