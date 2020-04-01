CREATE TABLE Utilizador (ID int(10) NOT NULL AUTO_INCREMENT, InscricaoID int(10) NOT NULL, Unidade_OrganicaID int(10), DepartamentoID int(10), Registo_HorarioID int(10) NOT NULL, Gestao_PerfilID int(10) NOT NULL, Email varchar(255), Nome varchar(255), Data_de_nascimento date, Numero_telemovel int(10), Cartao_cidadao int(10), Deficiencias varchar(255), Permitir_localizacao tinyint(1), Utilizar_dados_pessoais tinyint(1), Tema_do_website int(10), User_type int(10) NOT NULL, Daltonico tinyint(1), Validado tinyint(1) NOT NULL, Check_in_state tinyint(1) NOT NULL, PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Atividade (ID int(10) NOT NULL AUTO_INCREMENT, LocalID int(10) NOT NULL, UtilizadorID int(10) NOT NULL, UnidadeOrganicaID int(10) NOT NULL, Nome varchar(255), Descricao varchar(255), Duracao int(10), Limite_de_participantes int(10), Validada tinyint(1), Tipo_atividade varchar(255), Public_alvo varchar(255), PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Inscricao (ID int(10) NOT NULL AUTO_INCREMENT, EscolaID int(10), Dia date, PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Unidade_Organica (ID int(10) NOT NULL AUTO_INCREMENT, CampusID int(10) NOT NULL, Nome varchar(255), PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Sessao (ID int(10) NOT NULL AUTO_INCREMENT, Hora_de_inicio time, PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Tarefa (ID int(10) NOT NULL AUTO_INCREMENT, Sessao_Atividade_InscricaoID_Destino int(10), Sessao_Atividade_InscricaoID_Origem int(10) NOT NULL, UtilizadorID int(10) NOT NULL, Descricao varchar(255), Localizacao_do_grupo varchar(255), Destino varchar(255), Horario time, TarefaTransporte tinyint(1), PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Local (ID int(10) NOT NULL AUTO_INCREMENT, EdicifioID int(10) NOT NULL, Andar int(10), Sala int(10), Descricao varchar(255), Indoor tinyint(1), PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Edicifio (ID int(10) NOT NULL AUTO_INCREMENT, Num_edificio int(10), PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Campus (ID int(10) NOT NULL AUTO_INCREMENT, Nome varchar(255), Localizacao varchar(255), Contacto int(10), PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Notificacoes (ID int(10) NOT NULL AUTO_INCREMENT, UtilizadorID_Envia int(10) NOT NULL, UtilizadorID_Recebe int(10) NOT NULL, Conteudo varchar(255), Hora_envio time, Data date, Prioridade int(10), Assunto varchar(255), PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Escola (ID int(10) NOT NULL AUTO_INCREMENT, Nome varchar(255), Morada varchar(255), Zip int(10), Contacto int(10), Localidade varchar(255), PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Dia_Aberto (ID int(10) NOT NULL AUTO_INCREMENT, Titulo varchar(255), Descricao varchar(255), Email varchar(255), Contacto int(10), Data_inicio date, Data_fim date, Limite_de_inscricao_atividades date, Limite_de_inscricao_participantes date, PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Ementa (ID int(10) NOT NULL AUTO_INCREMENT, Dia date, Preco_economico_aluno double, Preco_normal_aluno double, Preco_economico_outro double, Preco_outro double, PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Departamento (ID int(10) NOT NULL AUTO_INCREMENT, Unidade_OrganicaID int(10) NOT NULL, Nome varchar(255), PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Tematica (ID int(10) NOT NULL AUTO_INCREMENT, Nome varchar(255), PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Atividade_Tematica (ID int(10) NOT NULL AUTO_INCREMENT, AtividadeID int(10) NOT NULL, TematicaID int(10) NOT NULL, PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Material (ID int(10) NOT NULL AUTO_INCREMENT, Nome varchar(255), PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Atividade_Material (ID int(10) NOT NULL AUTO_INCREMENT, AtividadeID int(10) NOT NULL, MaterialID int(10) NOT NULL, Quantidade int(10), PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Sessao_Atividade (ID int(10) NOT NULL AUTO_INCREMENT, SessaoID int(10) NOT NULL, AtividadeID int(10) NOT NULL, Data date, PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Sessao_Atividade_Inscricao (ID int(10) NOT NULL AUTO_INCREMENT, Sessao_AtividadeID int(10) NOT NULL, InscricaoID int(10) NOT NULL, Num_alunos int(10), PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Transporte (ID int(10) NOT NULL AUTO_INCREMENT, Hora_de_chegada time, Hora_de_partida time, Tipo_de_transporte varchar(255), Capacidade int(10), PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Horario (ID int(10) NOT NULL AUTO_INCREMENT, Hora_de_partida time, Data date, PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Transporte_Universitario_Horario (ID int(10) NOT NULL AUTO_INCREMENT, HorarioID int(10) NOT NULL, TransporteID int(10) NOT NULL, Origem varchar(255), Destino varchar(255), Data date, PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Prato (ID int(10) NOT NULL AUTO_INCREMENT, EmentaID int(10) NOT NULL, Nome varchar(255), Tipo varchar(255), Descricao varchar(255), PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Registo_Horario (ID int(10) NOT NULL AUTO_INCREMENT, Hora_inicio time, Hora_fim time, Data date, PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE ParticipanteInfo (ParticipanteInfoID int(10) NOT NULL AUTO_INCREMENT, UtilizadorID int(10) NOT NULL, Ano_escolar int(10) NOT NULL, Area varchar(255), Checkin_state tinyint(1) NOT NULL, Participante_type int(10), Total_de_participantes int(10), Total_de_professores int(10), Turma varchar(255), Autorizacao tinyint(1), Ficheiro_autorizacao varchar(255), Acompanhates int(10), TipoParticipante varchar(255), PRIMARY KEY (ParticipanteInfoID)) CHARACTER SET UTF8;
CREATE TABLE Tarefa_Sessao_Atividade (ID int(10) NOT NULL AUTO_INCREMENT, TarefaID int(10) NOT NULL, Sessao_AtividadeID int(10) NOT NULL, PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Utilizador_Transporte (ID int(10) NOT NULL AUTO_INCREMENT, UtilizadorID int(10) NOT NULL, TransporteID int(10) NOT NULL, PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Utilizador_Ementa (ID int(10) NOT NULL AUTO_INCREMENT, UtilizadorID int(10) NOT NULL, EmentaID int(10) NOT NULL, PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Utilizador_Tarefa (ID int(10) NOT NULL AUTO_INCREMENT, UtilizadorID int(10) NOT NULL, TarefaID int(10) NOT NULL, PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Inscricao_Ementa (ID int(10) NOT NULL AUTO_INCREMENT, InscricaoID int(10) NOT NULL, EmentaID int(10) NOT NULL, PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Utilizador_Atividade (ID int(10) NOT NULL AUTO_INCREMENT, UtilizadorID int(10) NOT NULL, AtividadeID int(10) NOT NULL, PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Atividade_Departamento (ID int(10) NOT NULL AUTO_INCREMENT, AtividadeID int(10) NOT NULL, DepartamentoID int(10) NOT NULL, PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Gestao_Perfil (ID int(10) NOT NULL AUTO_INCREMENT, Validacao tinyint(1), PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Dia_Aberto_Utilizador (ID int(10) NOT NULL AUTO_INCREMENT, Dia_AbertoID int(10) NOT NULL, UtilizadorID int(10) NOT NULL, PRIMARY KEY (ID)) CHARACTER SET UTF8;
CREATE TABLE Transporte_Universitario_Horario_Inscricao (ID int(10) NOT NULL AUTO_INCREMENT, Transporte_Universitario_HorarioID int(10) NOT NULL, InscricaoID int(10) NOT NULL, PRIMARY KEY (ID)) CHARACTER SET UTF8;
ALTER TABLE Utilizador ADD CONSTRAINT Pertence FOREIGN KEY (Unidade_OrganicaID) REFERENCES Unidade_Organica (ID);
ALTER TABLE Tarefa_Sessao_Atividade ADD CONSTRAINT Tem FOREIGN KEY (TarefaID) REFERENCES Tarefa (ID);
ALTER TABLE Tarefa_Sessao_Atividade ADD CONSTRAINT Tem2 FOREIGN KEY (Sessao_AtividadeID) REFERENCES Sessao_Atividade (ID);
ALTER TABLE Utilizador_Transporte ADD CONSTRAINT Gere FOREIGN KEY (UtilizadorID) REFERENCES Utilizador (ID);
ALTER TABLE Utilizador_Transporte ADD CONSTRAINT Gere2 FOREIGN KEY (TransporteID) REFERENCES Transporte (ID);
ALTER TABLE Utilizador_Ementa ADD CONSTRAINT Gere3 FOREIGN KEY (UtilizadorID) REFERENCES Utilizador (ID);
ALTER TABLE Utilizador_Ementa ADD CONSTRAINT Gere4 FOREIGN KEY (EmentaID) REFERENCES Ementa (ID);
ALTER TABLE Utilizador_Tarefa ADD CONSTRAINT Realiza FOREIGN KEY (UtilizadorID) REFERENCES Utilizador (ID);
ALTER TABLE Utilizador_Tarefa ADD CONSTRAINT Realiza2 FOREIGN KEY (TarefaID) REFERENCES Tarefa (ID);
ALTER TABLE Local ADD CONSTRAINT Pertence2 FOREIGN KEY (EdicifioID) REFERENCES Edicifio (ID);
ALTER TABLE Utilizador ADD CONSTRAINT Tem3 FOREIGN KEY (InscricaoID) REFERENCES Inscricao (ID);
ALTER TABLE Inscricao_Ementa ADD CONSTRAINT Tem4 FOREIGN KEY (InscricaoID) REFERENCES Inscricao (ID);
ALTER TABLE Inscricao_Ementa ADD CONSTRAINT Tem5 FOREIGN KEY (EmentaID) REFERENCES Ementa (ID);
ALTER TABLE Atividade ADD CONSTRAINT Gere5 FOREIGN KEY (UtilizadorID) REFERENCES Utilizador (ID);
ALTER TABLE Notificacoes ADD CONSTRAINT Envia_notificacao FOREIGN KEY (UtilizadorID_Envia) REFERENCES Utilizador (ID);
ALTER TABLE Notificacoes ADD CONSTRAINT Envia_notificacao2 FOREIGN KEY (UtilizadorID_Recebe) REFERENCES Utilizador (ID);
ALTER TABLE Tarefa ADD CONSTRAINT Gere6 FOREIGN KEY (UtilizadorID) REFERENCES Utilizador (ID);
ALTER TABLE Unidade_Organica ADD CONSTRAINT Localizada FOREIGN KEY (CampusID) REFERENCES Campus (ID);
ALTER TABLE Atividade ADD CONSTRAINT Localizada2 FOREIGN KEY (LocalID) REFERENCES Local (ID);
ALTER TABLE Utilizador_Atividade ADD CONSTRAINT Pedir_Alteracoes FOREIGN KEY (UtilizadorID) REFERENCES Utilizador (ID);
ALTER TABLE Utilizador_Atividade ADD CONSTRAINT Pedir_Alteracoes2 FOREIGN KEY (AtividadeID) REFERENCES Atividade (ID);
ALTER TABLE Sessao_Atividade ADD CONSTRAINT Pertence3 FOREIGN KEY (SessaoID) REFERENCES Sessao (ID);
ALTER TABLE Sessao_Atividade ADD CONSTRAINT Pertence4 FOREIGN KEY (AtividadeID) REFERENCES Atividade (ID);
ALTER TABLE Atividade_Tematica ADD CONSTRAINT Tem8 FOREIGN KEY (AtividadeID) REFERENCES Atividade (ID);
ALTER TABLE Atividade_Tematica ADD CONSTRAINT Tem6 FOREIGN KEY (TematicaID) REFERENCES Tematica (ID);
ALTER TABLE Atividade_Material ADD CONSTRAINT Pertence5 FOREIGN KEY (AtividadeID) REFERENCES Atividade (ID);
ALTER TABLE Atividade_Material ADD CONSTRAINT Pertence6 FOREIGN KEY (MaterialID) REFERENCES Material (ID);
ALTER TABLE Atividade_Departamento ADD CONSTRAINT Pertence7 FOREIGN KEY (AtividadeID) REFERENCES Atividade (ID);
ALTER TABLE Atividade_Departamento ADD CONSTRAINT Pertence8 FOREIGN KEY (DepartamentoID) REFERENCES Departamento (ID);
ALTER TABLE Inscricao ADD CONSTRAINT Preenche FOREIGN KEY (EscolaID) REFERENCES Escola (ID);
ALTER TABLE Sessao_Atividade_Inscricao ADD CONSTRAINT Tem10 FOREIGN KEY (Sessao_AtividadeID) REFERENCES Sessao_Atividade (ID);
ALTER TABLE Sessao_Atividade_Inscricao ADD CONSTRAINT Tem11 FOREIGN KEY (InscricaoID) REFERENCES Inscricao (ID);
ALTER TABLE Transporte_Universitario_Horario ADD CONSTRAINT Tem7 FOREIGN KEY (HorarioID) REFERENCES Horario (ID);
ALTER TABLE Transporte_Universitario_Horario ADD CONSTRAINT Tem9 FOREIGN KEY (TransporteID) REFERENCES Transporte (ID);
ALTER TABLE Prato ADD CONSTRAINT Tem14 FOREIGN KEY (EmentaID) REFERENCES Ementa (ID);
ALTER TABLE Utilizador ADD CONSTRAINT Pertence10 FOREIGN KEY (Registo_HorarioID) REFERENCES Registo_Horario (ID);
ALTER TABLE Tarefa ADD CONSTRAINT Destino FOREIGN KEY (Sessao_Atividade_InscricaoID_Destino) REFERENCES Sessao_Atividade_Inscricao (ID);
ALTER TABLE Departamento ADD CONSTRAINT Tem55 FOREIGN KEY (Unidade_OrganicaID) REFERENCES Unidade_Organica (ID);
ALTER TABLE Utilizador ADD CONSTRAINT Faz FOREIGN KEY (Gestao_PerfilID) REFERENCES Gestao_Perfil (ID);
ALTER TABLE Utilizador ADD CONSTRAINT Pertence9 FOREIGN KEY (DepartamentoID) REFERENCES Departamento (ID);
ALTER TABLE ParticipanteInfo ADD CONSTRAINT FKParticipan160823 FOREIGN KEY (UtilizadorID) REFERENCES Utilizador (ID);
ALTER TABLE Dia_Aberto_Utilizador ADD CONSTRAINT FKDia_Aberto547993 FOREIGN KEY (Dia_AbertoID) REFERENCES Dia_Aberto (ID);
ALTER TABLE Dia_Aberto_Utilizador ADD CONSTRAINT FKDia_Aberto820798 FOREIGN KEY (UtilizadorID) REFERENCES Utilizador (ID);
ALTER TABLE Transporte_Universitario_Horario_Inscricao ADD CONSTRAINT FKTransporte583721 FOREIGN KEY (Transporte_Universitario_HorarioID) REFERENCES Transporte_Universitario_Horario (ID);
ALTER TABLE Transporte_Universitario_Horario_Inscricao ADD CONSTRAINT FKTransporte86695 FOREIGN KEY (InscricaoID) REFERENCES Inscricao (ID);
ALTER TABLE Tarefa ADD CONSTRAINT Origem FOREIGN KEY (Sessao_Atividade_InscricaoID_Origem) REFERENCES Sessao_Atividade_Inscricao (ID);
ALTER TABLE Atividade ADD CONSTRAINT FKAtividade840442 FOREIGN KEY (UnidadeOrganicaID) REFERENCES Unidade_Organica (ID);
