import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { NestExpressApplication } from '@nestjs/platform-express'; // Importar el tipo NestExpressApplication

async function bootstrap() {
  // Crear el servidor de Nest usando Express
  const app = await NestFactory.create<NestExpressApplication>(AppModule);

  // Escuchar en el puerto (si existe, usa el valor de `PORT`, si no, usa 3000)
  await app.listen(process.env.PORT ?? 3000);
  console.log(`Servidor corriendo en http://localhost:${process.env.PORT ?? 3000}`);
}
bootstrap();
