CREATE TABLE [api].[api_key_auth](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[application_name] [nvarchar](50) NULL,
	[application_key] [nvarchar](250) NULL,
	[expiration_date] [datetime] not NULL,
 CONSTRAINT [api_key_auth_pk] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


insert into [DBA_IntergeaNE].api.api_key_auth (application_name, application_key,expiration_date) values ('GESTIONE_MULTE', 'JBEoXTiqZMc7NRxGARtRpgLmZkEZGna5LD','29990101');
