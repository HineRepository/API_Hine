USE [DBA_IntergeaNE]
GO

/****** Object:  View [bi].[geve_veicoli]    Script Date: 30/01/2025 12:57:12 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


create view [api].[api_veicoli] as
select
  v.[dim_veicolo] as dim_veicolo,
  da.Azienda as azienda_veicolo,
  [IdVeicolo] as id_gesionale_veicolo,
  v.[telaio] as telaio_veicolo,
  v.[targa] as targa_veicolo,
    v.[data_immatricolazione] as dt_immatricolazione_veicolo,
  data_arrivo as dt_arrivo_veicolo,
  data_consegna as dt_uscita_veicolo,
  gm.Descrizione gruppo_marca_veicolo,
  coalesce(v.[Modello], mm.descrmodello) modello_veicolo,
  [Veicolo] as veicolo,
  tv.DescrTipoVeicolo gruppo_tipo_veicolo,
  v.[alimentazione] as alimentazione_veicolo,
  Area as nuovo_usato_veicolo,
  fv.[status_veicolo_desc] as status_veicolo,
  [UbicazioneAttuale] as ubicazione_attuale_veicolo,
  [km_percorsi] as km_percorsi_veicolo,
  [Linea] as linea_veicolo
from
  ANAG_Auto_Veicolo_info v
  left join dbo.ANAG_TipoAlimentazione a on v.cod_alimentazione = a.CodiceTipoAlimentazione
  left join tree.Tree_Link_GruppoAlimentazione lga on lga.IdDimensione = a.__ID
  left join tree.TREE_GruppoAlimentazione ga on ga.IDRamo = lga.IdRamo
  left join dbo.ANAG_Auto_MarcaModello mm on v.cod_marca = mm.CodiceMarchio
  and v.cod_modello = mm.CodiceModello
  left join tree.Tree_Link_Auto_GruppoMarcaModello lgmm on lgmm.IdDimensione = mm.__ID
  left join tree.TREE_Auto_GruppoMarcaModello gmm on gmm.IDRamo = lgmm.IdRamo
  left join dbo.ANAG_Auto_Marca m on v.cod_marca = m.CodiceMarchio
  left join tree.Tree_Link_Auto_GruppoMarca lgm on lgm.IdDimensione = m.__ID
  left join tree.TREE_Auto_GruppoMarca gm on gm.IDRamo = lgm.IdRamo
  left join dbo.ANAG_TipoVeicolo tv on v.cod_tipo_veicolo = tv.CodiceTipoVeicolo
  left join tree.Tree_Link_GruppoTipoVeicolo ltv on ltv.IdDimensione = tv.__ID
  left join tree.TREE_GruppoAlimentazione gtv on gtv.IDRamo = ltv.IdRamo
  left join FATTI_Auto_Veicoli_INF fv on v.dim_veicolo = fv.dim_veicolo
  left join [bi].AUTO_dim_azienda da on da.dim_azienda=v.codice_azienda
GO


