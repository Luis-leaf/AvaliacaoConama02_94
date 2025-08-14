from django.db import models

class Fragmento(models.Model):
    
    # creating choices for CharField models
    CRESC_DOSSEL_CHOICES = [
        ('INICIAL', 'RAPIDO'),
        ('MEDIO', 'MODERADO'),
        ('AVANÇADO', 'LENTO'),
    ]

    VIDA_MEDIA_CHOICES = [
        ('INICIAL', 'CURTA'),
        ('MEDIO', 'MÉDIA'),
        ('AVANÇADO', 'LONGA'),
    ]

    AMPLI_DIAMETRICA_CHOICES = [
        ('INICIAL', 'PEQUENA'),
        ('MEDIO', 'MÉDIA'),
        ('AVANÇADO', 'GRANDE'),
    ]

    AMPLI_ALTURA_CHOICES = [
        ('INICIAL', 'PEQUENA'),
        ('MEDIO', 'MÉDIA'),
        ('AVANÇADO', 'GRANDE'),
    ]

    EPIFITAS_CHOICES = [
        ('INICIAL', 'RARAS'),
        ('MEDIO', 'POUCAS'),
        ('AVANÇADO', 'ABUNDANTE'),
    ]

    LIANAS_HERB_CHOICES = [
        ('INICIAL', 'ABUNDANTES'),
        ('MEDIO', 'POUCAS'),
        ('AVANÇADO', 'RARAS'),
    ]

    LIANAS_LENH_CHOICES = [
        ('INICIAL', 'AUSENTE'),
        ('MEDIO', 'RARA'),
        ('AVANÇADO', 'PRESENTE'),
    ]

    GRAMINEAS_CHOICES = [
        ('INICIAL', 'ABUNDANTES'),
        ('MEDIO', 'POUCAS'),
        ('AVANÇADO', 'RARAS'),
    ]

    REGEN_DOSSEL_CHOICES = [
        ('INICIAL', 'AUSENTE'),
        ('MEDIO', 'POUCA'),
        ('AVANÇADO', 'INTENSA'),
    ]

    #numeric data
    estratos = models.IntegerField(
        verbose_name="Estratos",
        help_text="Número de estratos do fragmento"
    )
    
    lenhosas = models.IntegerField(
        verbose_name="Lenhosas",
        help_text="Quantidade de plantas lenhosas"
    )

    area_basal = models.FloatField(
        verbose_name="Área Basal",
        help_text="Área basal do fragmento (m²/ha)"
    )
    
    altura_esp_dossel = models.FloatField(
        verbose_name="Altura Específica do Dossel",
        help_text="Altura específica do dossel (metros)"
    )
    
    med_ampli_diametros = models.FloatField(
        verbose_name="Média da Amplitude dos Diâmetros",
        help_text="Média da amplitude dos diâmetros (cm)"
    )
    
    dist_diametrica = models.FloatField(
        verbose_name="Distribuição Diamétrica",
        help_text="Valor da distribuição diamétrica"
    )

    #CharFields
    cresc_dossel = models.CharField(
        verbose_name="Crescimento do Dossel",
        help_text="Descrição do crescimento do dossel",
        choices=CRESC_DOSSEL_CHOICES,
        blank=True,
        null=True
    )
    
    vida_media = models.CharField(
        verbose_name="Vida Média",
        help_text="Informações sobre a vida média das espécies",
        choices=VIDA_MEDIA_CHOICES,
        blank=True,
        null=True
    )
    
    ampli_diametrica = models.CharField(
        verbose_name="Amplitude Diamétrica",
        help_text="Descrição da amplitude diamétrica",
        choices=AMPLI_DIAMETRICA_CHOICES,
        blank=True,
        null=True
    )
    
    ampli_altura = models.CharField(
        verbose_name="Amplitude de Altura",
        help_text="Descrição da amplitude de altura",
        choices=AMPLI_ALTURA_CHOICES,
        blank=True,
        null=True
    )
    
    epifitas = models.CharField(
        verbose_name="Epífitas",
        help_text="Informações sobre epífitas presentes",
        choices=EPIFITAS_CHOICES,
        blank=True,
        null=True
    )
    
    lianas_herb = models.CharField(
        verbose_name="Lianas Herbáceas",
        help_text="Descrição das lianas herbáceas",
        choices=LIANAS_HERB_CHOICES,
        blank=True,
        null=True
    )
    
    lianas_lenh = models.CharField(
        verbose_name="Lianas Lenhosas",
        help_text="Descrição das lianas lenhosas",
        choices=LIANAS_LENH_CHOICES,
        blank=True,
        null=True
    )
    
    gramineas = models.CharField(
        verbose_name="Gramíneas",
        help_text="Informações sobre gramíneas presentes",
        choices=GRAMINEAS_CHOICES,
        blank=True,
        null=True
    )
    
    regen_dossel = models.CharField(
        verbose_name="Regeneração do Dossel",
        help_text="Descrição da regeneração do dossel",
        choices=REGEN_DOSSEL_CHOICES,
        blank=True,
        null=True
    )

    #control data
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em"
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em"
    )

    class Meta: 
        verbose_name = "Fragmento"
        verbose_name_plural = "Fragmentos"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Fragmento {self.pk}"
    
    #Methods for evaluation of regeneration
    def avaliaParametro(self, valor, list_ref):
        
        if valor >= list_ref[0]:
            return "AVANÇADO"
        elif valor == list_ref[1]:
            return "INICIAL"
        else: return "MEDIO"
    

    
    def avaliaEstagio(self):
        pontuacao = {"INICIAL": 0,"MEDIO": 0,"AVANÇADO": 0 }
        
        #evaluation of numeric data:
        pontuacao[self.avaliaParametro(self.estratos,[2,1])] += 1
        pontuacao[self.avaliaParametro(self.lenhosas,[30,10])] += 1
        pontuacao[self.avaliaParametro(self.area_basal,[30,20])] += 1
        pontuacao[self.avaliaParametro(self.altura_esp_dossel,[30,10])] += 1
        pontuacao[self.avaliaParametro(self.med_ampli_diametros,[40,10])] += 1 

        #evaluation of categorical data:
        pontuacao[self.cresc_dossel] += 1
        pontuacao[self.vida_media] += 1
        pontuacao[self.ampli_diametrica] += 1
        pontuacao[self.ampli_altura] += 1
        pontuacao[self.epifitas] += 1
        pontuacao[self.lianas_herb] += 1
        pontuacao[self.lianas_lenh] += 1
        pontuacao[self.gramineas] += 1
        pontuacao[self.regen_dossel] += 1

        #retorn the result:
        return max(pontuacao, key=pontuacao.get)
