from django.db import models





# ---------- 2. About Section ----------
class AboutSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')
    students_enrolled = models.PositiveIntegerField(default=0)
    graduation_rate = models.FloatField(default=0.0)
    expert_faculty = models.PositiveIntegerField(default=0)
    mission_statement = models.TextField()

    def __str__(self):
        return self.title


# ---------- 3. Student Life Section ----------
class StudentLife(models.Model):
    section_title = models.CharField(max_length=100, default="Student Life")
    headline = models.CharField(max_length=250)
    description = models.TextField()
    main_image = models.ImageField(upload_to='student_life/')
    sub_image1 = models.ImageField(upload_to='student_life/', blank=True, null=True)
    sub_image2 = models.ImageField(upload_to='student_life/', blank=True, null=True)
    link_text = models.CharField(max_length=100, default="Explore Student Life")
    link_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.headline


# ---------- 4. News Section ----------
class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.CharField(max_length=50)
    image = models.ImageField(upload_to='news/')
    read_more_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.title}"


# ---------- 5. Gallery Section ----------
class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Gallery Image"


# ---------- 6. Footer Section ----------
class Footer(models.Model):
    site_name = models.CharField(max_length=100, default="MySchool")
    about_text = models.TextField(help_text="Short footer description text.")
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.site_name


class FooterLinkCategory(models.Model):
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, related_name="categories")
    title = models.CharField(max_length=100, help_text="e.g. 'Studio', 'Services', 'Resources', 'Connect'")

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    category = models.ForeignKey(FooterLinkCategory, on_delete=models.CASCADE, related_name="links")
    text = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.text


class HeroSlide(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    background_image = models.ImageField(upload_to='img/')
    button_text1 = models.CharField(max_length=50, blank=True, null=True)
    button_link1 = models.URLField(blank=True, null=True)
    button_text2 = models.CharField(max_length=50, blank=True, null=True)
    button_link2 = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title