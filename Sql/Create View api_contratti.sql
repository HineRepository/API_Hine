USE [DBA_IntergeaNE]
GO
    /****** Object:  View [api].[api_contratti]    Script Date: 02/02/2025 17:25:30 ******/
SET
    ANSI_NULLS ON
GO
SET
    QUOTED_IDENTIFIER ON
GO
    ALTER view [api].[api_contratti] as
SELECT
    con_codiceAzienda + '_' + [CON_IdContratto] as dim_contratto,
    f.dim_Veicolo as dim_veicolo,
    vi.targa as targa_contratto,
    vi.TELAIO as telaio_contratto,
    vi.IdVeicolo as id_gestionale_veicolo_contratto,
    left(con_idcontratto, 1) as nuovo_usato_contratto,
    format([CON_NumeroContratto], ' #######') as numero_contratto,
    gv.Descrizione as tipo_contratto,
    dim_ClienteAuto as dim_cliente,
    c.DescrizioneCliente as cliente_contratto,
    sede.sede as sede_contratto,
    ven.DescrVenditore as venditore_contratto,
    convert(date, [CON_DataApertura]) as dt_apertura_contratto,
    convert(date, [CON_DataChiusura]) as dt_chiusura_contratto,
    CON_FlagAssicurazioni as has_assicurazione_contratto,
    CON_FlagFinanziamento as has_finanziamento_contratto,
    [CON_NumeroPermute] as count_permute_contratto,
    CON_DescrStatoContratto as status_contratto
FROM
    [dbo].[FATTI_Auto_Contratti_INF] f
    inner join ANAG_Auto_Veicolo_info as vi on vi.dim_veicolo = f.dim_veicolo
    left outer join ANAG_Auto_TipoContratto tc on tc.__ID = dim_TipoContratto
    left join tree.Tree_Link_Auto_GruppoTipoContratto lv on tc.__ID = lv.IdDimensione
    left join tree.TREE_Auto_GruppoTipoContratto gv on gv.IDRamo = lv.IdRamo
    left outer join ANAG_Auto_ClienteAuto c on c.__ID = f.dim_ClienteAuto
    left outer join bi.AUTO_dim_sede sede on sede.dim_sede = f.dim_sede
    left outer join ANAG_Auto_Venditore ven on ven.__ID = f.dim_Venditore
union
SELECT
    con_codiceAzienda + '_' + [CON_IdContratto] as dim_contratto,
    f.dim_Veicolo as dim_veicolo,
    vi.targa as targa_contratto,
    vi.TELAIO as telaio_contratto,
    vi.IdVeicolo as id_gestionale_veicolo_contratto,
    left(con_idcontratto, 1) as nuovo_usato_contratto,
    format([CON_NumeroContratto], ' #######') as numero_contratto,
    gv.Descrizione as tipo_contratto,
    dim_ClienteAuto as dim_cliente,
    c.DescrizioneCliente as cliente_contratto,
    sede.sede as sede_contratto,
    ven.DescrVenditore as venditore_contratto,
    convert(date, [CON_DataApertura]) as dt_apertura_contratto,
    convert(date, [CON_DataChiusura]) as dt_chiusura_contratto,
    CON_FlagAssicurazioni as has_assicurazione_contratto,
    CON_FlagFinanziamento as has_finanziamento_contratto,
    [CON_NumeroPermute] as count_permute_contratto,
    CON_DescrStatoContratto as status_contratto
FROM
    [dbo].[FATTI_Auto_Contratti_STO] f
    inner join ANAG_Auto_Veicolo_info as vi on vi.dim_veicolo = f.dim_veicolo
    left outer join ANAG_Auto_TipoContratto tc on tc.__ID = dim_TipoContratto
    left join tree.Tree_Link_Auto_GruppoTipoContratto lv on tc.__ID = lv.IdDimensione
    left join tree.TREE_Auto_GruppoTipoContratto gv on gv.IDRamo = lv.IdRamo
    left outer join ANAG_Auto_ClienteAuto c on c.__ID = f.dim_ClienteAuto
    left outer join bi.AUTO_dim_sede sede on sede.dim_sede = f.dim_sede
    left outer join ANAG_Auto_Venditore ven on ven.__ID = f.dim_Venditore
GO